import numpy as np
from ..base import Indicator



class Extreme(Indicator):
    def __init__(self, slave, part, fraction):
        super().__init__()
        self.slave = slave
        assert part == 'lowest' or part == 'highest'
        self.part = part
        assert 0 < fraction and fraction <= 1
        self.quantile = fraction if part == 'lowest' else 1 - fraction
    
    def calculate(self, data):
        all_results = self.slave.calculate(data)
        border_value = np.nanquantile(all_results, self.quantile)
        masked_results = all_results.copy()
        if self.part == 'lowest':
            masked_results[masked_results > border_value] = np.nan
        else:
            masked_results[masked_results < border_value] = np.nan
        return masked_results


Indicator.extreme = lambda self, part, fraction: Extreme(self, part, fraction)
Indicator.lowest = lambda self, fraction: Extreme(self, 'lowest', fraction)
Indicator.highest = lambda self, fraction: Extreme(self, 'highest', fraction)