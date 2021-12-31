import unittest
import reprice
import pandas as pd
import numpy as np


def reprice_data():
    dates = pd.date_range(
        "2021-12-22",
        "2021-12-24",
        freq="D",
    ).astype(str)
    dates = list(dates)
    samples = [np.random.randint(25, 75) for _ in range(len(dates))]
    return pd.DataFrame.from_dict(dict(Y=samples, X=dates), orient="columns")


class TestReprice(unittest.TestCase):
    def test__set_initial_value(
        self,
    ):
        reprice_dataframe = reprice_data()
        reprice._get_returns(reprice_dataframe)
        reprice._set_initial_value(reprice_dataframe, 100, "reprice")
        self.assertEqual(reprice_dataframe["reprice"][0], 100)
