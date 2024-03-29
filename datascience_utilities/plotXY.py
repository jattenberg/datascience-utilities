# plotXY by @jattenberg, may 2012
#
# very simple alternative to gnuplot for plotting from the command line
# able to read from a file (using the -f option) or read from a pipe
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

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from statsmodels.nonparametric.smoothers_lowess import lowess

from .utils import option_parser, select_columns


def get_parser():
    parser = option_parser(
        """
    Generate a plot from columnar numeric data.
    If no x value is specified, the index is used.
    Usage %prog [options]
    """
    )

    parser.add_option(
        "-l",
        "--xlabel",
        dest="xlabel",
        action="store",
        default=False,
        help="label to use on the x axis",
    )
    parser.add_option(
        "-y",
        "--ylabel",
        action="store",
        dest="ylabel",
        default=False,
        help="label to use on the y axis",
    )
    parser.add_option(
        "-L",
        "--logscale",
        action="store_true",
        dest="log_scale",
        default=False,
        help="log scale values on both the x and y axis",
    )
    parser.add_option(
        "-X",
        "--semilogx",
        action="store_true",
        dest="semilogx",
        default=False,
        help="log scale values on the x axis",
    )
    parser.add_option(
        "-Y",
        "--semilogy",
        action="store_true",
        dest="semilogy",
        default=False,
        help="log scale values on the y axis",
    )
    parser.add_option(
        "-s",
        "--subplots",
        action="store_true",
        dest="subplots",
        default=False,
        help="use several subplots to represent data rather than multiple lines overlapped",  # noqa
    )
    parser.add_option(
        "-m",
        "--symbols",
        action="store_true",
        dest="symbols",
        default=False,
        help="use symbols to denote the actual data points in the plot",
    )
    parser.add_option(
        "-O",
        "--smoothing",
        action="store_true",
        dest="smoothing",
        default=False,
        help="smooth out the data using lowess regression",
    )
    parser.add_option(
        "-c",
        "--cumulative",
        action="store_true",
        dest="cum",
        default=False,
        help="store cumulative y values",
    )
    parser.add_option(
        "-x",
        "--xcol",
        dest="xcol",
        action="store",
        default=False,
        help="""use the specified column as the x-value
in the generated plot. Can be a column
name or column index (from 0)""",
    )
    parser.add_option(
        "-i",
        "--ignore",
        dest="ignore",
        action="store",
        help="""ignore the specified colums.
can be a column name or column index (from 0).
specifiy multiple values separated by commas""",
    )
    parser.add_option(
        "-C",
        "--columns",
        dest="columns",
        action="store",
        help="""include _only_ these columns.
can be a column name or column index (from 0).
specifiy multiple values separated by commas""",
    )

    parser.add_option(
        "-S",
        "--sort",
        action="store_false",
        dest="sort",
        default=True,
        help="don't sort data by the values in the x column",
    )

    return parser


def main():
    (options, args) = get_parser().parse_args()

    input = open(options.filename, "r") if options.filename else sys.stdin

    df = pd.read_csv(input, sep=options.delim, header=0 if options.header else None)

    if options.cum:
        df = df.cumsum()

    xcolumn = df.index
    count = df.shape[1]

    if options.xcol:
        count = df.shape[1] - 1
        if options.xcol in df.columns:
            xcolumn = df[options.xcol]
        elif options.xcol.isdigit() and int(options.xcol) < df.shape[1]:
            xcolumn = df.iloc[:, int(options.xcol)]
        else:
            raise LookupError("Unknown column: %s" % options.xcol)

    df = select_columns(df, options.ignore, options.columns, xcolumn)

    ycolumns = df.drop(xcolumn.name, axis=1) if options.xcol else df
    ycolumns.index = xcolumn

    if options.sort:
        ycolumns = ycolumns.sort_index()

    styles = ["-", "--", ".-", "s-", "o-", "^-"]
    colors = ["b", "r", "y", "k", "c", "m"]

    plt_styles = []
    for i in range(count):
        if options.symbols:
            style = styles[i % len(styles)]
        else:
            style = ""
        color = colors[i % len(colors)]
        plt_styles.append(color + style)

    if options.smoothing:
        for col in ycolumns.columns.values:
            ycolumns[col] = lowess(
                ycolumns[col].values, ycolumns.index, return_sorted=False, frac=0.05
            )

    ycolumns.plot(
        subplots=options.subplots,
        style=plt_styles,
        logx=options.semilogx or options.log_scale,
        logy=options.semilogy or options.log_scale,
    )

    plt.legend(loc="best")

    if options.ylabel is not False:
        plt.ylabel(options.ylabel)
    if options.xlabel is not False:
        plt.xlabel(options.xlabel)

    sns.set_style("darkgrid")

    if options.out:
        plt.savefig(options.out)
    else:
        plt.show()


if __name__ == "__main__":
    main()
