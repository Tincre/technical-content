import pytest
import pandas as pd
import numpy as np

# --------------------------------------------------------------------------- #
# TEST DATA MOCKS
# --------------------------------------------------------------------------- #
@pytest.fixture(scope="module")
def reprice_data():
    dates = pd.date_range(
        "2021-12-22",
        "2021-12-24",
        freq="D",
    ).astype(str)
    dates = list(dates)
    samples = [np.random.randint(25, 75) for _ in range(len(dates))]
    return dict(Y=samples, X=dates)


@pytest.fixture
def reprice_dataframe(reprice_data):
    return pd.DataFrame.from_dict(reprice_data, orient="columns")
