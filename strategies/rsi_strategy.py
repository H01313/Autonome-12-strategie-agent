from strategies.base_strategy import BaseStrategy
from utils.indicators import rsi


class RSIStrategy(BaseStrategy):
    def __init__(self, period=14):
        self.period = period

    def generate_signal(self, df):
        if len(df) < self.period:
            return "HOLD"

        df = df.copy()
        df["rsi"] = rsi(df, self.period)
        value = df["rsi"].iloc[-1]

        if value < 30:
            return "BUY"
        elif value > 70:
            return "SELL"

        return "HOLD"
