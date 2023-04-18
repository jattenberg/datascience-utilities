from optparse import OptionParser

import pandas as pd


def option_parser(usage):
    parser = OptionParser(usage=usage)

    parser.add_option(
        "-f",
        "--file",
        action="store",
        dest="filename",
        help="[optional] use a specified file instead of reading from stdin",
    )

    parser.add_option(
        "-H",
        "--header",
        action="store_true",
        dest="header",
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
        "-o",
        "--out",
        dest="out",
        action="store",
        default=False,
        help="[optional] file path for saving output",
    )

    return parser


def selector_parser(usage):
    parser = option_parser(usage)

    parser.add_option(
        "-i",
        "--ignore",
        dest="ignore",
        action="store",
        help="ignore the specified colums. can be a column name or column index (from 0). specifiy multiple values separated by commas",
    )
    parser.add_option(
        "-C",
        "--columns",
        dest="columns",
        action="store",
        help="include _only_ these columns. can be a column name or column index (from 0). specifiy multiple values separated by commas",
    )

    return parser


def select_columns(df, ignore, keep, xcolumn=None):
    if not ignore and not keep:
        return df

    if ignore and keep:
        raise ValueError(
            "must specify _either_ columns to ignore or columns to keep. you supplied both"
        )

    should_keep = bool(keep)
    specified = ignore.split(",") if ignore else keep.split(",")

    def _find_col(col):
        if col in df.columns:
            return df[col]
        elif col.isdigit() and int(col) < len(df.columns):
            return df.iloc[:, int(col)]
        else:
            raise LookupError("unknown column: %s" % col)

    out_cols = [_find_col(x) for x in specified] + (
        [xcolumn] if xcolumn is not None and keep else []
    )

    if keep:
        return df[[x.name for x in out_cols]]
    else:
        return df.drop([x.name for x in out_cols], axis=1)
