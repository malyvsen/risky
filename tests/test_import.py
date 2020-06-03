def test_top():
    import risky
    assert hasattr(risky, 'data')
    assert hasattr(risky, 'indicators')
    assert hasattr(risky.data, 'fetch')
    assert hasattr(risky.data, 'universe')
    assert hasattr(risky.indicators, 'Returns')