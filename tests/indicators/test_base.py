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
    def assert_count(self, original, extreme):
        values = original(None)
        for i in range(len(values) + 1):
            fraction = i / len(values)
            extreme_values = extreme(fraction)(None)
            assert np.sum(~extreme_values.isna()) == i

    def test_low(self):
        self.assert_count(FakeIndicator(), FakeIndicator().lowest)
        assert np.nanmin(FakeIndicator().lowest(0.5)(None)) == 1
        assert np.nanmax(FakeIndicator().lowest(0.5)(None)) == 4

    def test_high(self):
        self.assert_count(FakeIndicator(), FakeIndicator().highest)
        assert np.nanmin(FakeIndicator().highest(0.5)(None)) == 5
        assert np.nanmax(FakeIndicator().highest(0.5)(None)) == 8