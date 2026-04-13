class StrategyEngine:
    def __init__(self, strategies, weights=None, threshold=1):
        self.strategies = strategies
        self.weights = weights if weights else [1]*len(strategies)
        self.threshold = threshold

    def get_signal(self, df):
        score = 0

        for strat, w in zip(self.strategies, self.weights):
            signal = strat.generate_signal(df)

            if signal == "BUY":
                score += w
            elif signal == "SELL":
                score -= w

        # 🔥 TRADE FILTER (BELANGRIJK)
        if score > self.threshold:
            return "BUY"
        elif score < -self.threshold:
            return "SELL"

        return "HOLD"
