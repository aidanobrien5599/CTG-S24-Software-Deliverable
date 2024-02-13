import numpy as np
import pandas as pd
import os
import yfinance as yf

root_path = 'task_1/data'

with open('task_1/tickers.txt', 'r') as file:
    tickers = file.read().splitlines()

start_date = "2021-01-01"
end_date = "2023-12-31"

# Function to handle date-time formatting
def format_date(date_str):
    return pd.to_datetime(date_str).strftime('%m/%d/%Y')

data = ''

df = pd.DataFrame()

for ticker in tickers:
    #use yf.download, which will grab each data point we are looking for from yfinance
    data = yf.download(ticker, start=start_date, end=end_date)
    
    
    close  = np.array(data['Close'])
    close_5_days_ago = np.array(data['Close'])
    close_5_days_ago = np.roll(close_5_days_ago, 5)
    momentum = ((close - close_5_days_ago))*100
    momentum[:5] = np.nan
    df[ticker] = momentum

df.index = data.index

df.to_csv('task_2/price_momentum/price_momentum.csv')
    
    
    
    