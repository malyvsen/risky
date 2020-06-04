import numpy as np
from risky.data import fetch
from risky.indicators.base import Indicator
from risky.indicators import Close



def test_basic():
    assert isinstance(Close().log(), Indicator)

def test_single():
    data = fetch.ohlcv('AAPL')
    log_close = Close().log()(data)
    assert_single(data, log_close)

def test_multi():
    data = fetch.ohlcv('AAPL TSLA')
    log_close = Close().log()(data)
    for symbol in data.columns.levels[0]:
        assert_single(data[symbol], log_close[symbol])


def assert_single(data, log_close):
    assert np.all(log_close.index == data.index)
    manual_log_close = np.log(data.close)
    assert np.all(log_close.values == manual_log_close)