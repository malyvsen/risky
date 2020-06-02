import numpy as np
import pandas as pd
from risky.data import fetch
from risky.indicators.base import Indicator
from risky.indicators import Returns


class FakeIndicator(Indicator):
    def calculate(self, data):
        arr = np.array([1, 2, 3, 4, 5, 6, 7, 8], dtype=float)
        return pd.Series(arr)


class TestLog:
    def assert_single(self, data, log_returns):
        assert np.all(log_returns.index == data.index)
        assert np.isnan(log_returns.iloc[0])
        manual_log_returns = data.close[1:].values / data.close[:-1].values
        assert np.all(log_returns.values[1:] == np.log(manual_log_returns))
    
    def test_basic(self):
        assert isinstance(FakeIndicator().log(), Indicator)

    def test_single(self):
        data = fetch.ohlcv('AAPL')
        log_returns = Returns().log()(data)
        self.assert_single(data, log_returns)

    def test_multi(self):
        data = fetch.ohlcv('AAPL TSLA')
        log_returns = Returns().log()(data)
        for symbol in data.columns.levels[0]:
            self.assert_single(data[symbol], log_returns[symbol])

class TestExtreme:
    def test_low(self):
        fake = FakeIndicator()
        fake_values = fake(None)
        for i in range(len(fake_values) + 1):
            fraction = i / len(fake_values)
            lowest = fake.lowest(fraction)(None)
            assert np.sum(~lowest.isna()) == i

    def test_high(self):
        fake = FakeIndicator()
        fake_values = fake(None)
        for i in range(len(fake_values) + 1):
            fraction = i / len(fake_values)
            highest = fake.highest(fraction)(None)
            assert np.sum(~highest.isna()) == i