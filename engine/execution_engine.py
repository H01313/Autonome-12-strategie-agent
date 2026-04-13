class ExecutionEngine:
    def __init__(self):
        self.balance = 1000
        self.position = 0
        self.entry_price = 0
        self.fee = 0.001

    def execute(self, signal, price):
        if signal == "BUY" and self.position == 0:
            self.position = (self.balance * (1 - self.fee)) / price
            self.entry_price = price
            self.balance = 0
            print(f"BUY @ {price}")

        elif self.position > 0:
            change = (price - self.entry_price) / self.entry_price

            if signal == "SELL" or change <= -0.02 or change >= 0.04:
                self.balance = self.position * price * (1 - self.fee)
                self.position = 0
                print(f"SELL @ {price}")
