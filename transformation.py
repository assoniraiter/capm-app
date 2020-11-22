import numpy as np
import pandas as pd

# Function to obtain daily returns
def get_returns(df):
    """
    Function to obtain logarithmic returns.
    df: Data containing raw values.
    """
    # Performing logarithmic variation
    data = (np.log(df) - np.log(df.shift(1))).dropna()
    
    return data

# Function to obtain excess values
def get_excess(df, riskfree, name):
    """
    Function to obtain excess returns.
    df: Data containing ticker/market returns.
    """
    # Joining data and dropping NaNs.
    df = pd.concat([df, riskfree], axis = 1).dropna()
    # Renaming columns
    df.columns = ['ticker/market', 'riskfree']
    # Creating new column: excess return
    df[name] = df['ticker/market'] - df['riskfree']
    # Dropping unnecessary columns
    df.drop(['ticker/market', 'riskfree'], axis = 1, inplace = True)
    
    return df

