def rsi(df, period=14):
    delta = df["close"].diff()

    gain = delta.clip(lower=0).rolling(period).mean()
    loss = -delta.clip(upper=0).rolling(period).mean()

    rs = gain / (loss + 1e-10)
    rsi_values = 100 - (100 / (1 + rs))

    return rsi_values


def bollinger_bands(df, period=20, num_std=2):
    sma = df["close"].rolling(period).mean()
    std = df["close"].rolling(period).std()

    upper_band = sma + (std * num_std)
    lower_band = sma - (std * num_std)

    return upper_band, lower_band
