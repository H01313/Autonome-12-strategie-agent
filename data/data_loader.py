import ccxt
import pandas as pd
from config.config import EXCHANGE


class DataLoader:
    def __init__(self):
        exchange_class = getattr(ccxt, EXCHANGE)
        self.exchange = exchange_class({
            "enableRateLimit": True
        })

    def fetch_ohlcv(self, symbol, timeframe, limit=500):
        data = self.exchange.fetch_ohlcv(symbol, timeframe, limit=limit)

        df = pd.DataFrame(
            data,
            columns=["timestamp", "open", "high", "low", "close", "volume"]
        )

        # 🔥 CRUCIALE FIXES
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

        df = df.drop_duplicates()
        df = df.sort_values("timestamp")

        # Zorg dat alles numeriek is
        numeric_cols = ["open", "high", "low", "close", "volume"]
        df[numeric_cols] = df[numeric_cols].astype(float)

        df = df.reset_index(drop=True)

        return df
