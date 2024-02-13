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
    
    #numpy highs and lows of the day
    high  = np.array(data.loc[:, "High"])
    low = np.array(data.loc[:, "Low"])
    
    #calcute daily average between high and low
    daily_average = (high+low)/2
    #get average from nine days prior
    daily_average_9_days_ago = np.roll(daily_average, 9)
    
    
    #get the momentum coming into the next day
    momentum = (daily_average-daily_average_9_days_ago)/daily_average_9_days_ago*100
    #roll that momentum forward
    momentum = np.roll(momentum, 1)
    #first 10 values are invalid
    momentum[:10] = np.nan
    df[ticker] = momentum

# Set the index of df to match the index of data
df.index = data.index

df.to_csv('task_2/daily_averaged_momentum/daily_averaged_momentum.csv')
    
    