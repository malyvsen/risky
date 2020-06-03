import numpy as np
import pandas as pd
from risky.indicators.base import Indicator



def test_extreme():
    assert np.nanmin(FakeIndicator().extreme('lowest', 0.5)(None)) == 1
    assert np.nanmax(FakeIndicator().extreme('lowest', 0.5)(None)) == 4
    assert np.nanmin(FakeIndicator().extreme('highest', 0.5)(None)) == 5
    assert np.nanmax(FakeIndicator().extreme('highest', 0.5)(None)) == 8

def test_low():
    assert_count(FakeIndicator(), FakeIndicator().lowest)
    assert np.nanmin(FakeIndicator().lowest(0.5)(None)) == 1
    assert np.nanmax(FakeIndicator().lowest(0.5)(None)) == 4

def test_high():
    assert_count(FakeIndicator(), FakeIndicator().highest)
    assert np.nanmin(FakeIndicator().highest(0.5)(None)) == 5
    assert np.nanmax(FakeIndicator().highest(0.5)(None)) == 8

def test_nan():
    class FakeIndicator(Indicator):
        def calculate(self, data):
            arr = np.array([1, np.nan, 2, np.nan, 3])
            return pd.Series(arr)
    assert np.nanmin(FakeIndicator().lowest(0.5)(None)) == 1
    assert np.nanmax(FakeIndicator().lowest(0.5)(None)) == 2
    assert np.nanmin(FakeIndicator().highest(0.5)(None)) == 2
    assert np.nanmax(FakeIndicator().highest(0.5)(None)) == 3
    assert np.sum(~FakeIndicator().lowest(0.5)(None).isna()) == 2
    assert np.sum(~FakeIndicator().lowest(1)(None).isna()) == 3


class FakeIndicator(Indicator):
    def calculate(self, data):
        arr = np.array([1, 2, 3, 4, 5, 6, 7, 8], dtype=float)
        return pd.Series(arr)

def assert_count(original, extreme):
    values = original(None)
    for i in range(1, len(values) + 1):
        fraction = i / len(values)
        extreme_values = extreme(fraction)(None)
        assert np.sum(~extreme_values.isna()) == i