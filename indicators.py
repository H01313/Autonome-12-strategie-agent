def rsi(df, period=14):
    delta = df['close'].diff()

    gain = delta.clip(lower=0).rolling(period).mean()
    loss = -delta.clip(upper=0).rolling(period).mean()

    rs = gain / (loss + 1e-10)  # FIX division by zero
    rsi = 100 - (100 / (1 + rs))

    return rsi
