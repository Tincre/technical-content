"""
reprice.py

A simple pipeline to "reprice" a security. Give it a frame with 'X' and 'Y' plus 
a starting value, like 100, and get back that security at your starting value.

>>> from reprice import reprice
>>> reprice(df,100, inplace=True)
>>> ndf = reprice(df, 100)
>>> ndf.head()

By Ella (Xinxin) Li and Jason R. Stevens, CFA on behalf of Tincre. 

All rights reserved.
"""
from typing import Optional, Union
import pandas as pd


def _set_initial_value(
    df: pd.DataFrame, initial_value: Union[int, float], column: str = "reprice"
) -> None:
    """Set the given column with an initial value from returns."""
    df[column] = df["returns"] + 1  # more performant than a lambda
    df.loc[0, column] = initial_value


def _propogate_initial_value(
    df: pd.DataFrame, column: str = "reprice"
) -> None:
    """
    Return the cumulative product of the given column.
    """
    df[column] = df[column].cumprod()


def _get_returns(df: pd.DataFrame) -> None:
    """
    Return the percent change of 'Y'.
    """
    df["returns"] = df["Y"].pct_change()


def _copy_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return a deep copy of the given DataFrame `df`.
    """
    return df.copy(deep=True)


def reprice(
    df: pd.DataFrame, starting_value: Union[int, float], inplace: bool = False
) -> Optional[pd.DataFrame]:
    """
    Reprice the value in column 'Y' from DataFrame `df` and `starting_value`.
    """
    if not inplace:
        _df = _copy_dataframe(df)
        _get_returns(_df)
        _set_initial_value(
            _df,
            starting_value,
        )
        _propogate_initial_value(
            _df,
        )
        return _df

    _get_returns(df)
    _set_initial_value(df, starting_value)
    _propogate_initial_value(df)
