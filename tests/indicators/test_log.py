import numpy as np
from risky.data import fetch
from risky.indicators.base import Indicator
from risky.indicators import Returns



class TestLog:
    def assert_single(self, data, log_returns):
        assert np.all(log_returns.index == data.index)
        assert np.isnan(log_returns.iloc[0])
        manual_log_returns = data.close[1:].values / data.close[:-1].values
        assert np.all(log_returns.values[1:] == np.log(manual_log_returns))
    
    def test_basic(self):
        assert isinstance(Returns().log(), Indicator)

    def test_single(self):
        data = fetch.ohlcv('AAPL')
        log_returns = Returns().log()(data)
        self.assert_single(data, log_returns)

    def test_multi(self):
        data = fetch.ohlcv('AAPL TSLA')
        log_returns = Returns().log()(data)
        for symbol in data.columns.levels[0]:
            self.assert_single(data[symbol], log_returns[symbol])