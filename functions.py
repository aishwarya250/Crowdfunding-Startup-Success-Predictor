"""
Copyright (c) 2019
Licensed
Written by <Jigar Panchal>
"""

import pandas as pd

def eda_missing_nunique(df):
    datatype = df.dtypes
    missing_values = df.isnull().sum()
    percent_missing = df.isnull().sum() * 100 / len(df)
    nunique = list(df.nunique())
    total_len = len(df)
    count_df = pd.DataFrame({'Data type': datatype,'Total number of values':total_len,'Total Missing Values': missing_values,'Percentage missing': percent_missing, ' Count of unique values': nunique})
    return count_df
