from ..base import Indicator



class Diff(Indicator):
    def __init__(self, slave, period=1):
        super().__init__()
        self.slave = slave
        self.period = period
    
    def calculate(self, data):
        return self.slave.calculate(data).diff(periods=self.period)


Indicator.diff = lambda self: Diff(self)