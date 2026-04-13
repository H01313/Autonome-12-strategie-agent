class RiskManager:
    def __init__(self, risk_per_trade=0.02):
        self.risk_per_trade = risk_per_trade

    def position_size(self, balance):
        return balance * self.risk_per_trade
