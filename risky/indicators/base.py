import numpy as np
import pandas as pd



class Indicator:
    def __init__(self):
        pass

    def calculate(self, data):
        '''
        Should calculate the indicator values for each point in time, filling with NaN where needed.
        :param data: A Pandas DataFrame with columns named 'open', 'high', 'low', 'close', and 'volume'
        :return: The calculated values in a Pandas Series indexed by time.
        '''
        raise NotImplementedError()
    
    def __call__(self, data):
        if isinstance(data, pd.DataFrame):
            if isinstance(data.columns, pd.MultiIndex):
                result = {}
                for symbol in data.columns.levels[0]:
                    result[symbol] = self.calculate(data[symbol])
                return pd.DataFrame.from_dict(result)
        return self.calculate(data)

    def log(self):
        slave = self
        class Log(Indicator):
            def calculate(self, data):
                return np.log(slave.calculate(data))
        return Log()
    
    def lowest(self, fraction):
        return self.extreme(part='lowest', fraction=fraction)
    
    def highest(self, fraction):
        return self.extreme(part='highest', fraction=fraction)
    
    def extreme(self, part, fraction):
        assert part == 'lowest' or part == 'highest'
        slave = self
        quantile = fraction if part == 'lowest' else 1 - fraction
        class Extreme(Indicator):
            def calculate(self, data):
                all_results = slave.calculate(data)
                if fraction == 0:
                    result = all_results.copy()
                    result[:] = np.nan
                    return result
                border_value = np.nanquantile(all_results, quantile)
                masked_results = all_results.copy()
                if part == 'lowest':
                    masked_results[masked_results > border_value] = np.nan
                else:
                    masked_results[masked_results < border_value] = np.nan
                return masked_results
        return Extreme()
    
    def fillna(self, value=None, method=None, limit=None):
        slave = self
        class FillNA(Indicator):
            def calculate(self, data):
                return slave.calculate(data).fillna(value=value, method=method, limit=limit)
        return FillNA()