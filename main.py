from data.data_loader import DataLoader
from strategies.rsi_strategy import RSIStrategy
from strategies.bollinger_strategy import BollingerStrategy
from engine.strategy_engine import StrategyEngine
from backtesting.backtester import Backtester
from engine.execution_engine import ExecutionEngine

SYMBOL = "BTC/USDT"
TIMEFRAME = "1h"

if __name__ == "__main__":
    loader = DataLoader()

    df = loader.fetch_ohlcv(SYMBOL, TIMEFRAME, limit=1000)

    # DROP NaN (CRUCIAAL)
    df = df.dropna().reset_index(drop=True)

    strategies = [RSIStrategy(), BollingerStrategy()]
    weights = [1.2, 1.0]

    strategy_engine = StrategyEngine(strategies, weights, threshold=1)

    # BACKTEST
    backtester = Backtester()
    result = backtester.run(df, strategy_engine)

    print(f"Backtest final balance: {result}")

    # PAPER TRADING
    execution_engine = ExecutionEngine()

    for i in range(100, len(df)):
        sub_df = df.iloc[:i].copy()
        price = df["close"].iloc[i]

        signal = strategy_engine.get_signal(sub_df)
        execution_engine.execute(signal, price)

    print(f"Final balance: {execution_engine.balance}")
