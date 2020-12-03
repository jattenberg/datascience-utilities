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

import pandas as pd

from .utils import option_parser

def get_parser():
    parser = option_parser("""consume json data and emit it back as a csv""")

    parser.add_option(
        "-O",
        "--orient",
        action="store",
        dest="orient",
        default="records",
        help="""Indication of expected JSON string format.\n
                      default is `records`.
                      The set of possible orients is:\n

    'split' : dict like {index -> [index], columns -> [columns], data -> [values]}\n

    'records' : list like [{column -> value}, ... , {column -> value}]\n

    'index' : dict like {index -> {column -> value}}\n

    'columns' : dict like {column -> {index -> value}}\n

    'values' : just the values array
""",
    )

    parser.add_option(
        "-i",
        "--index",
        action="store_true",
        dest="index",
        help="add a column <index> with the row number",
    )

    parser.add_option(
        "-L",
        "--lines",
        action="store_true",
        dest="lines",
        help="read line-delimited json",
    )

    parser.add_option(
        "-C",
        "--columns",
        action="store_true",
        dest="columns",
        help="print the column names and exit"
    )

    return parser


def main():
    (options, args) = get_parser().parse_args()

    input = open(options.filename, "r") if options.filename else sys.stdin
    output = open(options.out, "w") if options.out else sys.stdout

    df = pd.read_json(input, orient=options.orient, lines=options.lines)

    if options.columns:
        output.write(options.delim.join(df.columns.values))
        return
    
    df.to_csv(
        output,
        sep=options.delim,
        index=options.index,
        index_label="index" if options.index else False,
    )


if __name__ == "__main__":
    main()
