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

import pandas as pd

from .utils import select_columns, selector_parser


def get_parser():
    parser = selector_parser(
        "selects or ignores the supplied fields. Supports indices or column names if a header is supplied. similar to the linux command `cut`"
    )

    parser.add_option(
        "-I",
        "--index",
        action="store_true",
        dest="index",
        help="add a column <index> with the row number",
    )

    return parser


def main():
    (options, args) = get_parser().parse_args()

    input = open(options.filename, "r") if options.filename else sys.stdin

    out = open(options.out, "w") if options.out else sys.stdout

    df = pd.read_csv(input, sep=options.delim, header=0 if options.header else None)

    df = select_columns(df, options.ignore, options.columns)

    df.to_csv(
        out,
        sep=options.delim,
        index=options.index,
        index_label="index" if options.index else False,
    )


if __name__ == "__main__":
    main()
