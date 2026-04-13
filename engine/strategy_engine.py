class StrategyEngine:
    def __init__(self, strategies, weights, threshold=1):
        self.strategies = strategies
        self.weights = weights
        self.threshold = threshold

    def get_signal(self, df):
        score = 0

        for strategy, weight in zip(self.strategies, self.weights):
            signal = strategy.generate_signal(df)

            if signal == "BUY":
                score += weight
            elif signal == "SELL":
                score -= weight

        if score >= self.threshold:
            return "BUY"
        elif score <= -self.threshold:
            return "SELL"

        return "HOLD"
