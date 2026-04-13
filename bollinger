def bollinger_bands(df, period=20):
    sma = df['close'].rolling(period).mean()
    std = df['close'].rolling(period).std()

    upper = sma + 2 * std
    lower = sma - 2 * std

    return upper, lower
