import numpy as np
import pandas as pd
import os
import yfinance as yf

root_path = 'task_1/data'

#get tick names
with open('task_1/tickers.txt', 'r') as file:
    tickers = file.read().splitlines()

df = pd.DataFrame()

for ticker in tickers:
    # Use cleaned data from prev csv file
    data = pd.read_csv(root_path + "/" + ticker + ".csv", index_col=0)  # Set index_col to 0 to use the first column as index
    
    close  = np.array(data.loc[:, "Close"])
    
    open = np.array(data.loc[:, "Open"])
    open_4_days_ago = np.roll(open, 4)
    
    momentum = ((((close - open_4_days_ago)))/open_4_days_ago) * 100
    momentum[:5] = np.nan
    df[ticker] = momentum

# Set the index of df to match the index of data
df.index = data.index

df.to_csv('task_2/price_momentum/price_momentum.csv')
    
    