import pandas as pd
from risky.data import fetch



class TestOHLCV:
    def assert_ohlcv(self, df):
        if isinstance(df.columns, pd.MultiIndex):
            df = df.reorder_levels(order=[1, 0], axis=1)
        assert 'open' in df
        assert 'high' in df
        assert 'low' in df
        assert 'close' in df
        assert 'volume' in df
    
    def assert_monthish(self, df):
        assert len(df) < 25
        assert len(df) > 15

    def test_single(self):
        fetched = fetch.ohlcv('AAPL', period='1mo', interval='1d')
        self.assert_monthish(fetched)
        self.assert_ohlcv(fetched)
    
    def test_spaced(self):
        fetched = fetch.ohlcv('AAPL TSLA', period='1mo', interval='1d')
        self.assert_monthish(fetched)
        self.assert_ohlcv(fetched)
    
    def test_list(self):
        fetched = fetch.ohlcv(['AAPL', 'TSLA'], period='1mo', interval='1d')
        self.assert_monthish(fetched)
        self.assert_ohlcv(fetched)
