def get_data(df, cols, asc=True, sort=True):
    datasets = []
    keys = []
    for col in cols:
        r = df.groupby(col).size()
        if sort:
            r = r.sort_values(ascending=asc)
        datasets.append({"label": col, "data": r.to_list(), "borderWidth": 1})
        keys = r.keys().to_list()

    return {"labels": keys, "datasets": datasets}


def get_chart(allData, chartTitle, chartType="bar", indexAxis="x"):
    return {
        "type": chartType,
        "data": allData,
        "options": {
            "indexAxis": indexAxis,
            "scales": {indexAxis: {"beginAtZero": True}},
            "layout": {"padding": 30},
            "plugins": {
                "title": {
                    "display": True,
                    "text": chartTitle,
                    "padding": {
                        "top": 10,
                        "bottom": 20,
                    },
                    "color": "#92A0A7",
                }
            },
        },
    }


def get_chart_for_fintech_type_status_chart(df):
    data = df.groupby("Status").size().sort_values()
    key_list = data.keys().to_list()
    datasets = []
    for key in key_list:
        d = (
            df[df["Status"] == key]
            .groupby("Subsegment")
            .size()
            .sort_values(ascending=False)
        )

        datasets.append(
            {
                "label": key,
                "data": d.to_list(),
                "borderWidth": 1,
            }
        )

    return {
        "labels": df.groupby("Subsegment").size().keys().to_list(),
        "datasets": datasets,
    }


def get_charts(df):
    if len(df) == 0:
        return []

    status_bar_chart = get_chart(
        get_data(df, ["Status"]),
        "Status: FinTech is active vs inactive",
        indexAxis="y",
    )
    fintech_type_pie_chart = get_chart(
        get_data(df, ["Segment"]), "Frequecy of FinTech by segment type", "pie"
    )
    other_fin_techs = get_chart(
        get_data(df[df["Segment"] == "Other FinTechs"], ["Subsegment"]),
        "Break down of Other FinTech segment",
        indexAxis="y",
    )
    year_bar_chart = get_chart(
        get_data(df, ["Year"], sort=False), "FinTech Companies Count by Founding Year"
    )
    all_fintech_type_chart = get_chart(
        get_data(df, ["Subsegment"]), "Frequecy of FinTech by all types", "line"
    )
    fintech_type_status_chart = get_chart(
        get_chart_for_fintech_type_status_chart(df),
        "Frequency of FinTech subsegments: Active vs Inactive",
        indexAxis="y",
    )
    country_chart = get_chart(
        get_data(df, ["Country"], asc=False), "Fintech density by location (Country)"
    )
    mixed_chart = get_chart(
        get_data(df, ["Insolvency", "Liquidation", "Bank Cooperation"]),
        "Insolvency, Liquidation and Bank Cooperation in FinTech Companies",
    )

    return [
        status_bar_chart,
        fintech_type_pie_chart,
        other_fin_techs,
        year_bar_chart,
        all_fintech_type_chart,
        fintech_type_status_chart,
        country_chart,
        mixed_chart,
    ]
