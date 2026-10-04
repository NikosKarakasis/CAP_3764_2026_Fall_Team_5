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

def quartile_limits(df):

    """

    Removes outliers from SeoulBikeData.csv columns.
    
    Using the Q1, Q2, and IQR taken from the dataframe,
    Tukey's fence rule is used to find the upper and
    lowe limits of columns.

    Parameters
    ----------
    path: DataFrame
        Path to the CSV file or specific columns. Can only
        handle quantitative columns.

    Returns
    -------
    pandas.DataFrame
        The upper and lower limits of columns.

    """

    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR
    return lower_limit, upper_limit