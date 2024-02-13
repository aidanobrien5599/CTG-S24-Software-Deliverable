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
    
    high  = np.array(data.loc[:, "High"])
    low = np.array(data.loc[:, "Low"])
    
    daily_average = (high+low)/2
    daily_average_10_days_ago = np.roll(daily_average, 10)
    
    

    momentum = (daily_average-daily_average_10_days_ago)/daily_average_10_days_ago*100
    momentum[:10] = np.nan
    df[ticker] = momentum

# Set the index of df to match the index of data
df.index = data.index

df.to_csv('task_2/daily_averaged_momentum/daily_averaged_momentum.csv')
    
    