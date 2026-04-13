import ccxt
import pandas as pd


class DataLoader:
    def __init__(self):
        self.exchange = ccxt.binance({
            "enableRateLimit": True
        })

    def fetch_ohlcv(self, symbol, timeframe, limit=500):
        try:
            data = self.exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
        except Exception as e:
            print("ERROR fetching data:", e)
            return pd.DataFrame()

        df = pd.DataFrame(
            data,
            columns=["timestamp", "open", "high", "low", "close", "volume"]
        )

        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
        df = df.drop_duplicates()
        df = df.sort_values("timestamp")

        return df
