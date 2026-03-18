class RiskManager:
    def __init__(self, balance):
        self.balance = balance
        self.daily_loss = 0
        self.trades = 0

    def can_trade(self):
        if self.daily_loss <= -self.balance * 0.05:
            return False
        if self.trades >= 25:
            return False
        return True

    def position_size(self):
        return self.balance * 0.02

    def update(self, pnl):
        self.balance += pnl
        self.daily_loss += pnl
        self.trades += 1
