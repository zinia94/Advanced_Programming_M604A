from src.charts import get_data, get_chart, get_chart_for_fintech_type_status_chart
import pandas as pd
import pytest


@pytest.mark.parametrize(
    "test_column, expected_output",
    [
        (
            "col1",
            {
                "labels": [0, 1, 2, 3],
                "datasets": [{"borderWidth": 1, "data": [1, 1, 1, 1], "label": "col1"}],
            },
        ),
        (
            "col3",
            {
                "labels": ["a", "b", "c", "d"],
                "datasets": [{"borderWidth": 1, "data": [1, 1, 1, 1], "label": "col3"}],
            },
        ),
    ],
)
def test_get_data(test_column, expected_output):
    df = pd.DataFrame(
        {"col1": [0, 1, 2, 3], "col2": [5, 6, 7, 8], "col3": ["a", "b", "c", "d"]}
    )
    assert get_data(df, [test_column]) == expected_output


def test_get_chart():
    data = {
        "labels": ["a", "b", "c", "d"],
        "datasets": [{"borderWidth": 1, "data": [1, 1, 1, 1], "label": "col3"}],
    }
    actual = {
        "type": "pie",
        "data": data,
        "options": {
            "indexAxis": "y",
            "scales": {"y": {"beginAtZero": True}},
            "layout": {"padding": 30},
            "plugins": {
                "title": {
                    "display": True,
                    "text": "test title",
                    "padding": {
                        "top": 10,
                        "bottom": 20,
                    },
                    "color": "#92A0A7",
                }
            },
        },
    }
    assert get_chart(data, "test title", "pie", "y") == actual


def test_get_chart_for_fintech_type_status_chart():
    df = pd.DataFrame({"Status": [0, 1, 2, 3], "Subsegment": [5, 6, 7, 8]})
    actual = {
        "datasets": [
            {"borderWidth": 1, "data": [1], "label": 0},
            {"borderWidth": 1, "data": [1], "label": 1},
            {"borderWidth": 1, "data": [1], "label": 2},
            {"borderWidth": 1, "data": [1], "label": 3},
        ],
        "labels": [5, 6, 7, 8],
    }
    assert get_chart_for_fintech_type_status_chart(df) == actual
