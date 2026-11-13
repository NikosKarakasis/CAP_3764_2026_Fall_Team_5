import pandas as pd

def load_seoul_bike_data(file_path):

    """
    
    Load the SeoulBikeData.csv dataset from a CSV file.

    The function encoding cp949 tells pandas to interpret
    the bytes in standard windows Korean code.

    Changes "Date" column from it's dtype to a standardized
    datetime objects.

    Replaces the names of each column with it's same name in
    underscore by hand and changes some Korean symbols into
    US-style letters.

    Parameters
    ----------
    df: DataFrame
        Path to the CSV file.

    Returns
    -------
    pandas.DataFrame
        The standardized "Date" column, and the new names
        of the columns in lowercase in US-style. The loaded 
        SeoulBikeData.csv dataset interpreted in korean code.

    """

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