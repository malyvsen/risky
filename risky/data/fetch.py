import yfinance



def ohlcv(tickers, period='1y', interval='1d'):
    data = yfinance.download(tickers, period=period, interval=interval, auto_adjust=True)
    data = data[~data.index.duplicated()]
    data.rename(
        columns={name: name.lower() for name in ['Open', 'High', 'Low', 'Close', 'Volume']},
        level=0,
        inplace=True
    )
    return data