import pandas as pd


def select_columns(df, ignore, keep, xcolumn=None):
    if not ignore and not keep:
        return df

    if ignore and keep:
        raise ValueError("must specify _either_ columns to ignore or columns to keep. you supplied both")

    should_keep = bool(keep)
    specified = ignore.split(",") if ignore else keep.split(",")

    def _find_col(col):
        if col in df.columns:
            return df[col]
        elif col.isdigit() and int(col) < len(df.columns):
            return df.iloc[:, int(col)]
        else:
            raise LookupError("unknown column: %s" % col)

    out_cols = [_find_col(x) for x in specified]\
        + ([xcolumn] if xcolumn is not None and keep else [])

    if keep:
        return df[[x.name for x in out_cols]]
    else:
        return df.drop([x.name for x in out_cols], axis=1)
