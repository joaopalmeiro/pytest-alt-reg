def test_example(chart_regression):
    contents = {"contents": "Foo", "value": 11}
    chart_regression.check(contents)
