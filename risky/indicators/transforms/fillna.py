import numpy as np
from ..base import Indicator


    
class FillNA(Indicator):
    def __init__(self, slave, value=None, method=None, limit=None):
        super().__init__()
        self.slave = slave
        self.value = value
        self.method = method
        self.limit = limit

    def calculate(self, data):
        return self.slave.calculate(data).fillna(
            value=self.value,
            method=self.method,
            limit=self.limit
        )


def fillna(*args, **kwargs):
    return FillNA(*args, **kwargs)

Indicator.fillna = fillna