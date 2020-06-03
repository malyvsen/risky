import numpy as np
import pandas as pd
from risky.indicators.base import Indicator



def test_value():
    class FakeIndicator(Indicator):
        def calculate(self, data):
            arr = np.array([1, 2, 3, np.nan])
            return pd.Series(arr)
    assert np.all(FakeIndicator().fillna(0)(None).values == [1, 2, 3, 0])
    assert np.all(FakeIndicator().fillna(-7)(None).values == [1, 2, 3, -7])

def test_ffill():
    class FakeIndicator(Indicator):
        def calculate(self, data):
            arr = np.array([1, np.nan, 2, np.nan, np.nan])
            return pd.Series(arr)
    assert np.all(FakeIndicator().fillna(method='ffill')(None).values == [1, 1, 2, 2, 2])
    assert np.isnan(FakeIndicator().fillna(method='ffill', limit=1)(None).iloc[-1])

def test_bfill():
    class FakeIndicator(Indicator):
        def calculate(self, data):
            arr = np.array([np.nan, np.nan, 2, np.nan, 3])
            return pd.Series(arr)
    assert np.all(FakeIndicator().fillna(method='bfill')(None).values == [2, 2, 2, 3, 3])
    assert np.isnan(FakeIndicator().fillna(method='bfill', limit=1)(None).iloc[0])