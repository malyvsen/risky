import numpy as np
import pandas as pd
from risky.indicators.base import Indicator



def test_period_one():
    class FakeIndicator(Indicator):
        def calculate(self, data):
            return pd.Series([1, 2, 1, 4])
    fake_values = FakeIndicator().ratio(1)(None)
    assert np.isnan(fake_values[0])
    assert fake_values[1] == 2
    assert fake_values[2] == 0.5
    assert fake_values[3] == 4

def test_period_two():
    class FakeIndicator(Indicator):
        def calculate(self, data):
            return pd.Series([1, 2, 1, 4])
    fake_values = FakeIndicator().ratio(2)(None)
    assert np.all(np.isnan(fake_values[0:2]))
    assert fake_values[2] == 1
    assert fake_values[3] == 2