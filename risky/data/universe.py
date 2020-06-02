import pandas as pd



sp500 = pd.read_csv('https://datahub.io/core/s-and-p-500-companies/r/constituents.csv')
sp500 = [symbol.replace('.', '-') for symbol in sp500.Symbol]