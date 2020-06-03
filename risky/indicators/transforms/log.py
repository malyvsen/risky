import numpy as np
from ..base import Indicator



class Log(Indicator):
    def __init__(self, slave):
        super().__init__()
        self.slave = slave
    
    def calculate(self, data):
        return np.log(self.slave.calculate(data))


Indicator.log = lambda self: Log(self)