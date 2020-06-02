from risky.data import universe



class TestSP500:
    def test_count(self):
        assert len(universe.sp500) == 505
    
    def test_aapl(self):
        assert 'AAPL' in universe.sp500