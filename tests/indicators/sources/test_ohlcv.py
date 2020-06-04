import numpy as np
from risky.data import fetch
from risky.indicators import Open, High, Low, Close, Volume



def test_single():
    data = fetch.ohlcv('AAPL')
    open = Open()(data)
    high = High()(data)
    low = Low()(data)
    close = Close()(data)
    volume = Volume()(data)
    assert np.all(open == data['open'])
    assert np.all(high == data['high'])
    assert np.all(low == data['low'])
    assert np.all(close == data['close'])
    assert np.all(volume == data['volume'])

def test_multi():
    data = fetch.ohlcv('AAPL TSLA')
    open = Open()(data)
    high = High()(data)
    low = Low()(data)
    close = Close()(data)
    volume = Volume()(data)
    for symbol in data.columns.levels[0]:
        assert np.all(open[symbol] == data[symbol, 'open'])
        assert np.all(high[symbol] == data[symbol, 'high'])
        assert np.all(low[symbol] == data[symbol, 'low'])
        assert np.all(close[symbol] == data[symbol, 'close'])
        assert np.all(volume[symbol] == data[symbol, 'volume'])