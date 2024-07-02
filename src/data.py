import pandas as pd


def prepare_data(df):
    # data preparation
    df["Founding year"] = pd.to_datetime(df["Founding year"], format="%Y")
    df["Year"] = df["Founding year"].dt.year
    df = df.astype(
        {"Liquidation": str, "Insolvency": str, "Bank Cooperation": str, "Status": str}
    )
    df.loc[df["Status"] == "0", "Status"] = "Inactive"
    df.loc[df["Status"] == "1", "Status"] = "Active"
    df.loc[df["Bank Cooperation"] == "0", "Bank Cooperation"] = "No"
    df.loc[df["Bank Cooperation"] == "1", "Bank Cooperation"] = "Yes"
    df.loc[df["Insolvency"] == "0", "Insolvency"] = "No"
    df.loc[df["Insolvency"] == "1", "Insolvency"] = "Yes"
    df.loc[df["Liquidation"] == "0", "Liquidation"] = "No"
    df.loc[df["Liquidation"] == "1", "Liquidation"] = "Yes"

    return df


def get_filtered_data(df, from_date, to_date):
    filterd_Df = df[df["Founding year"].dt.date >= from_date]
    return filterd_Df[filterd_Df["Founding year"].dt.date <= to_date]


def get_records_replace_nan(df):
    r = df.astype(str)
    for column in r:
        r.loc[r[column] == "nan", column] = ""
    return list(r.values)
