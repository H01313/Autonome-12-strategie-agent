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
        price = df['close'].iloc[i]

        signal = strategy_engine.get_signal(sub_df)
        execution_engine.execute(signal, price)

    print(f"Final balance: {execution_engine.balance}")
