import pandas as pd

def make_features(df_raw: pd.DataFrame) -> pd.DataFrame:
    """Create a supervised learning feature set from the raw Seoul Bike dataframe."""
    df_feat = pd.DataFrame()
    # Target series
    s = df_raw["rented_bike_count"].asfreq("h").ffill()
    df_feat["count"] = s

    # Calendar features (Seasonality)
    idx = s.index
    df_feat["hour"] = idx.hour
    df_feat["dayofweek"] = idx.dayofweek
    df_feat["month"] = idx.month

    # Lags (Autocorrelation & Seasonality)
    for lag in [1, 2, 24, 168]:
        df_feat[f"lag_{lag}"] = s.shift(lag)

    # Rolling means (Only use past information)
    df_feat["roll_mean_24"] = s.shift(1).rolling(24).mean()
    df_feat["roll_mean_168"] = s.shift(1).rolling(168).mean()

    # Covariates
    for col in [ "temperature_c", "humidity","wind_speed", "visibility","dew_point_temperature_c","solar_radiation","rainfall","snowfall","season","holiday",
        "functioning_day"]:
        if col in df_raw.columns:
            df_feat[col] = df_raw[col].asfreq("h").ffill()

    # Remove rows with missing values
    df_feat.dropna(inplace=True)

    return df_feat