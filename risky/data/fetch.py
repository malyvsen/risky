import pandas as pd
import yfinance



def ohlcv(tickers, period='1y', interval='1d'):
    data = yfinance.download(tickers, period=period, interval=interval, auto_adjust=True, group_by='ticker')
    data = data[~data.index.duplicated()]
    data.rename(
        columns={name: name.lower() for name in ['Open', 'High', 'Low', 'Close', 'Volume']},
        level=1 if isinstance(data.columns, pd.MultiIndex) else 0,
        inplace=True
    )
    return data