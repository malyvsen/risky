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