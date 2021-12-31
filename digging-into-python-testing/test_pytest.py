import reprice
import pandas as pd
import multiply


def test_reprice(reprice_dataframe):
    ndf = reprice.reprice(reprice_dataframe, 200)
    assert isinstance(ndf, pd.DataFrame)
    assert ndf["Y"][0] == reprice_dataframe["Y"][0]
    assert not reprice.reprice(ndf, 1, inplace=True)


def test_multiply():
    assert isinstance(multiply.multiply_int(1, 0), int)
    assert multiply.multiply_int(20, 10) == 200
