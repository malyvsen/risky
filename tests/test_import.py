def test_top():
    import risky
    assert hasattr(risky, 'data')
    assert hasattr(risky, 'indicators')
    assert hasattr(risky.data, 'fetch')
    assert hasattr(risky.data, 'universe')
    assert hasattr(risky.indicators, 'Column')
    assert hasattr(risky.indicators, 'Open')
    assert hasattr(risky.indicators, 'High')
    assert hasattr(risky.indicators, 'Low')
    assert hasattr(risky.indicators, 'Close')
    assert hasattr(risky.indicators, 'Volume')