import altair as alt


def test_bar_chart(chart_regression):
    source = alt.pd.DataFrame(
        {
            "a": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
            "b": [28, 55, 43, 91, 81, 53, 19, 87, 52],
        }
    )

    chart = alt.Chart(source).mark_bar().encode(x="a", y="b")

    chart_regression.check(chart)
