from .base import Indicator



class Returns(Indicator):
    '''Returns in terms of close_prices[t] / close_price[t-1]'''
    def __init__(self):
        super().__init__()
    
    def calculate(self, data):
        return data.close.pct_change() + 1