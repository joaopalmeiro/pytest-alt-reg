def test_bar_chart(chart_regression):
    contents = {"contents": "Foo", "value": 11}
    chart_regression.check(contents)
