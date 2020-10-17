import pandas as pd


def select_columns(df, ignore, keep, xcolumn=None):
    if not ignore and not keep:
        return df

    if ignore and keep:
        raise ValueError("must specify _either_ columns to ignore or columns to keep. you supplied both")

    should_keep = bool(keep)
    specified = ignore.split(",") if ignore else keep.split(",")

    all_cols = df.columns

    out_cols = [xcolumn] if xcolumn is not None and keep else []

    for col in specified:
        if col in all_cols:
            out_cols.append(df[col])
        elif col.isdigit() and int(col) < len(all_cols):
            out_cols.append(df.iloc[:, int(col)])
        else:
            raise LookupError("unknown column: %s" % col)

    if keep:
        return df[[x.name for x in out_cols]]
    else:
        return df.drop([x.name for x in out_cols], axis=1)
