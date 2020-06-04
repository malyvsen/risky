from ..base import Indicator



class Ratio(Indicator):
    def __init__(self, slave, period=1):
        super().__init__()
        self.slave = slave
        self.period = period
    
    def calculate(self, data):
        return 1 + self.slave.calculate(data).pct_change(
            periods=self.period,
            fill_method=None
        )


Indicator.ratio = lambda self, period: Ratio(self, period)