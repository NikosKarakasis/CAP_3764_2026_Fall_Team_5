import pandas as pd

def read_data (path):
    df = pd.read_csv(path, encoding="cp949")
    return df

def data_prep(df):
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
    
    df = df.rename(columns={
    "Date": "date",
    "Rented Bike Count": "rented_bike_count",
    "Hour": "hour",
    "Temperature(캜)": "temperature_c",
    "Humidity(%)": "humidity",
    "Wind speed (m/s)": "wind_speed",
    "Visibility (10m)": "visibility",
    "Dew point temperature(캜)": "dew_point_temperature_c",
    "Solar Radiation (MJ/m2)": "solar_radiation",
    "Rainfall(mm)": "rainfall",
    "Snowfall (cm)": "snowfall",
    "Seasons": "season",
    "Holiday": "holiday",
    "Functioning Day": "functioning_day"
    })

    return df

def quartile_limits(df):
    pass
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 - 1.5 * IQR
    return lower_limit, upper_limit

    

# print(df.head())
