import pandas as pd


def load_seoul_bike_data(file_path):

    df = pd.read_csv(file_path, encoding="cp949")

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