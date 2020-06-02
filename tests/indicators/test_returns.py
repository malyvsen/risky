import numpy as np
from risky.data import fetch
from risky.indicators import Returns



class TestReturns:
    def assert_single(self, data, returns):
        assert np.all(returns.index == data.index)
        assert np.isnan(returns.iloc[0])
        manual_returns = data.close[1:].values / data.close[:-1].values
        assert np.all(returns.values[1:] == manual_returns)

    def test_single(self):
        data = fetch.ohlcv('AAPL')
        returns = Returns()(data)
        self.assert_single(data, returns)

    def test_multi(self):
        data = fetch.ohlcv('AAPL TSLA')
        returns = Returns()(data)
        for symbol in data.columns.levels[0]:
            self.assert_single(data[symbol], returns[symbol])