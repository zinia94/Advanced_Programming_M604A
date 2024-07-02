from src.data import get_data


def test_get_data():
    df = get_data()
    assert sorted(df["Status"].unique().tolist()) == ["Active", "Inactive"]
    assert sorted(df["Bank Cooperation"].unique().tolist()) == ["No", "Yes"]
    assert sorted(df["Insolvency"].unique().tolist()) == ["No", "Yes"]
    assert sorted(df["Liquidation"].unique().tolist()) == ["No", "Yes"]
