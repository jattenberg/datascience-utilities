#!/usr/local/bin/python
"""
Copyright (c) 2013 Josh Attenberg

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""


import sys
from optparse import OptionParser

import numpy as np
import pandas as pd
from scipy.stats import bayes_mvs, normaltest, sem, stats

from .utils import select_columns


def get_nonnumeric(column, np_values):

    data = np_values.describe()
    output = [present("Column", column)]
    for id in data.index:
        output.append(present(id.capitalize(), data[id]))
    return output


def get_data(column, np_values, options):

    alpha = float(options.alpha)
    mvs = bayes_mvs(np_values, alpha)

    # report these metrics
    output = [
        present("Column", column),
        present("Length", len(np_values)),
        present("Unique", len(np.unique(np_values))),
        present("Min", np_values.min()),
        present("Max", np_values.max()),
        present("Sum", np_values.sum()),
        present("Mid-Range", (np_values.max() - np_values.min()) / 2),
        present("Range", np_values.max() - np_values.min()),
        present("Mean", np_values.mean()),
        present("Mean-%s-CI" % alpha, tupleToString(mvs[0][1])),
        present("Variance", mvs[1][0]),
        present("Var-%s-CI" % alpha, tupleToString(mvs[1][1])),
        present("StdDev", mvs[2][0]),
        present("Std-%s-CI" % alpha, tupleToString(mvs[2][1])),
        present("Mode", stats.mode(np_values)[0][0]),
        present("Q1", stats.scoreatpercentile(np_values, 25)),
        present("Q2", stats.scoreatpercentile(np_values, 50)),
        present("Q3", stats.scoreatpercentile(np_values, 75)),
        present("Trimean", trimean(np_values)),
        present("Minhinge", midhinge(np_values)),
        present("Skewness", stats.skew(np_values)),
        present("Kurtosis", stats.kurtosis(np_values)),
        present("StdErr", sem(np_values)),
        present("Normal-P-value", normaltest(np_values)[1]),
    ]
    return output


# this prints a bit nicer than tuples standard toString
def tupleToString(tuple):
    return "(%s, %s)" % tuple


def present(key, value):
    return key + " : " + str(value)


def trimean(values):
    return (
        stats.scoreatpercentile(values, 25)
        + 2.0 * stats.scoreatpercentile(values, 50)
        + stats.scoreatpercentile(values, 75)
    ) / 4.0


def midhinge(values):
    return (
        stats.scoreatpercentile(values, 25) + stats.scoreatpercentile(values, 75)
    ) / 2.0


def relations(df, num_columns):
    return [
        "\nCovariances:",
        str(df[num_columns].cov()),
        "\nCorrelations:",
        str(df[num_columns].corr()),
    ]


def gather_descriptions(df, options):
    def _is_numeric(col):
        return df[col].dtype.kind == "i" or df[col].dtype.kind == "f"

    def _describe_column(col):
        if _is_numeric(col):
            return get_data(col, df[col], options)
        else:
            return get_nonnumeric(col, df[col])

    description = ["\n".join(_describe_column(c)) for c in df.columns]
    num_columns = list(filter(_is_numeric, df.columns))

    if not options.simple and df.shape[1] > 1 and len(num_columns) > 1:
        return description + relations(df, num_columns)
    else:
        return description


def get_parser():
    parser = OptionParser(
        usage="""presents a range of standard descriptive statistics
    on columns of numerical data
    perl -e 'for($i = 0; $i < 20; $i++){print rand(), "\\t", rand(), "\\t", rand(), "\\n"}' | python describe.py
    Usage %prog [options]
    """  # noqa
    )

    parser.add_option(
        "-f",
        "--file",
        action="store",
        dest="filename",
        default=False,
        help="[optional] use a specified file instead of reading from stdin",
    )
    parser.add_option(
        "-o",
        "--out",
        action="store",
        dest="out",
        default=False,
        help="[optional] write to a specified file instead of stdout",
    )
    parser.add_option(
        "-H",
        "--header",
        action="store_true",
        dest="header",
        default=None,
        help="treat the first row as column headers",
    )
    parser.add_option(
        "-d",
        "--delim",
        action="store",
        dest="delim",
        default="\t",
        help="delimiter seperating columns in input",
    )
    parser.add_option(
        "-a",
        "--alpha",
        action="store",
        dest="alpha",
        default=0.9,
        help="confidence value used in interval estimation",
    )
    parser.add_option(
        "-s",
        "--simple",
        action="store_true",
        dest="simple",
        default=False,
        help="abbreviated, simplified output",
    )
    parser.add_option(
        "-i",
        "--ignore",
        dest="ignore",
        action="store",
        help="""ignore the specified colums. can be a column name or column index (from 0).
specifiy multiple values separated by commas""",  # noqa,
    )
    parser.add_option(
        "-C",
        "--columns",
        dest="columns",
        action="store",
        help="""include _only_ these columns. can be a column name or column index (from 0).
specifiy multiple values separated by commas""",  # noqa,
    )

    return parser


def main():

    (options, args) = get_parser().parse_args()

    input = open(options.filename, "r") if options.filename else sys.stdin

    out = open(options.out, "w") if options.out else sys.stdout

    df = pd.read_csv(input, sep=options.delim, header=0 if options.header else None)

    df = select_columns(df, options.ignore, options.columns)

    description = gather_descriptions(df, options)

    out.write("\n\n".join(description) + "\n")
    out.flush()
    out.close()
    input.close()


if __name__ == "__main__":
    main()
