class BaseStrategy:
    def generate_signal(self, df):
        raise NotImplementedError("Strategy must implement generate_signal()")
