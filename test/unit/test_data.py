from src.data import prepare_data
import pandas as pd


def test_prepare_data():
    df = pd.DataFrame(
        {
            "Status": [0, 1, 0, 1],
            "Bank Cooperation": [0, 1, 1, 0],
            "Insolvency": [0, 1, 1, 0],
            "Liquidation": [1, 1, 0, 1],
            "Founding year": [2012.0, 2011.0, 2013.0, 2014.0],
        }
    )
    df = prepare_data(df)
    assert sorted(df["Status"].unique().tolist()) == ["Active", "Inactive"]
    assert sorted(df["Bank Cooperation"].unique().tolist()) == ["No", "Yes"]
    assert sorted(df["Insolvency"].unique().tolist()) == ["No", "Yes"]
    assert sorted(df["Liquidation"].unique().tolist()) == ["No", "Yes"]
    assert sorted(df["Year"].unique().tolist()) == [2011, 2012, 2013, 2014]
