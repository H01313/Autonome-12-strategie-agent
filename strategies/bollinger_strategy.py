from strategies.base_strategy import BaseStrategy
from utils.indicators import bollinger_bands


class BollingerStrategy(BaseStrategy):
    def __init__(self, period=20):
        self.period = period

    def generate_signal(self, df):
        # Zorg dat er genoeg data is
        if len(df) < self.period:
            return "HOLD"

        upper, lower = bollinger_bands(df, self.period)

        # Pak laatste waarden
        price = df["close"].iloc[-1]
        upper_band = upper.iloc[-1]
        lower_band = lower.iloc[-1]

        # Check op NaN (komt vaak voor bij rolling windows)
        if upper_band is None or lower_band is None:
            return "HOLD"

        if price < lower_band:
            return "BUY"
        elif price > upper_band:
            return "SELL"

        return "HOLD"
