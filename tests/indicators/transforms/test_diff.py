import numpy as np
import pandas as pd
from risky.indicators.base import Indicator



def test_period_one():
    class FakeIndicator(Indicator):
        def calculate(self, data):
            return pd.Series([1, 2, 3, 5])
    fake_values = FakeIndicator()(None).diff(1)
    assert np.isnan(fake_values[0])
    assert np.all(fake_values[1:3] == 1)
    assert fake_values[3] == 2

def test_period_two():
    class FakeIndicator(Indicator):
        def calculate(self, data):
            return pd.Series([1, 2, 3, 5])
    fake_values = FakeIndicator()(None).diff(2)
    assert np.all(np.isnan(fake_values[0:2]))
    assert fake_values[2] == 2
    assert fake_values[3] == 3