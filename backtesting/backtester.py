class Backtester:
    def run(self, df, strategy_engine, initial_balance=1000):
        balance = initial_balance
        position = 0
        entry_price = 0
        fee = 0.001

        for i in range(50, len(df)):
            sub_df = df.iloc[:i].copy()
            price = df["close"].iloc[i]

            signal = strategy_engine.get_signal(sub_df)

            if signal == "BUY" and position == 0:
                position = (balance * (1 - fee)) / price
                entry_price = price
                balance = 0

            elif position > 0:
                change = (price - entry_price) / entry_price

                if change <= -0.02 or change >= 0.04 or signal == "SELL":
                    balance = position * price * (1 - fee)
                    position = 0

        if position > 0:
            balance = position * df["close"].iloc[-1] * (1 - fee)

        return balance
