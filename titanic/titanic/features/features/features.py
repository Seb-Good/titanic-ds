"""Methods to create engineed features."""

import pandas as pd

def age_bin(df):
    df['age_bin'] = pd.cut(df['age'], list(range(0, int(df['age'].max()), 10)))
    return df
