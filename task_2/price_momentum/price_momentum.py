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
    
    close  = np.array(data.loc[:, "Close"]) # get close array
    
    open = np.array(data.loc[:, "Open"]) #get open array
    open_4_days_ago = np.roll(open, 4) #roll if forward 4 days
    
    momentum = ((((close - open_4_days_ago)))/open_4_days_ago) * 100 #calculate momentum
    momentum[:5] = np.nan #first 5 data points are invalid
    df[ticker] = momentum

# Set the index of df to match the index of data
df.index = data.index

df.to_csv('task_2/price_momentum/price_momentum.csv') #convert it to csv    
    
    