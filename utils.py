import pandas as pd
import numpy as np


def horizontal_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def decdeg2dms(dd):
    negative = dd < 0
    dd = abs(dd)
    minutes,seconds = divmod(dd*3600,60)
    degrees,minutes = divmod(minutes,60)
    if negative:
        if degrees > 0:
            degrees = -degrees
        elif minutes > 0:
            minutes = -minutes
        else:
            seconds = -seconds
    return (degrees,minutes,seconds)


def decdeg2dms_string(dd, round_to_nearest_int=True, pad_with_zeros=True):
    d, m, s = decdeg2dms(dd)

    if round_to_nearest_int:
        d, m, s = [int(round(n)) for n in (d, m, s)]

    if pad_with_zeros:
        d, m, s = str(d), str(m), str(s)
        if len(m) == 1:
            m = '0' + m
        if len(s) == 1:
            s = '0' + s

    dms_string = "{}°{}'{}\"".format(d, m, s)

    return dms_string


def clipboard_to_clipboard(sep=','):
    current_clipboard = pd.read_clipboard()
    current_clipboard.to_clipboard(sep=sep, index=False)


def dataframe_to_clipboard(df, sep=','):
    df.to_clipboard(sep=sep, index=False)
