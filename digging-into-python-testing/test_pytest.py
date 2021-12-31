import reprice
import pandas as pd
import multiply
import numpy as np


def test_reprice(reprice_dataframe):
    ndf = reprice.reprice(reprice_dataframe, 200)
    assert isinstance(ndf, pd.DataFrame)
    assert ndf["Y"][0] == reprice_dataframe["Y"][0]
    assert not reprice.reprice(ndf, 1, inplace=True)


def test__propogate_initial_value(reprice_dataframe):
    """Remember to include the previous pieces which have been tested since they are related."""
    reprice._get_returns(reprice_dataframe)
    reprice._set_initial_value(reprice_dataframe, 100, "reprice")
    reprice._propogate_initial_value(reprice_dataframe, "reprice")
    ind = np.random.randint(0, len(reprice_dataframe))
    assert reprice_dataframe["reprice"][ind] > 0


def test_multiply():
    assert isinstance(multiply.multiply_int(1, 0), int)
    assert multiply.multiply_int(20, 10) == 200
