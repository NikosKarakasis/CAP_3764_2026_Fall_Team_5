import pandas as pd

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