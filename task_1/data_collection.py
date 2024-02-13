import numpy as np
import pandas as pd
import os
import yfinance as yf

#get tickers from file 
with open('task_1/tickers.txt', 'r') as file:
    tickers = file.read().splitlines()

# Define the directory where CSV files will be saved
output_directory = 'task_1/data/'

# Define the date range
start_date = "2021-01-01"
end_date = "2023-12-31"



#getting every ticker from ticker.txt
for ticker in tickers:
    #use yf.download, which will grab each data point we are looking for from yfinance
    data = yf.download(ticker, start=start_date, end=end_date)
    
    #convert it to a pandas datafram
    df = pd.DataFrame(data, index=data.index)  # Set index here
    
    # Handle missing values
    df.fillna(method='ffill', inplace=True)  # Fill with previous values

    ## changing to the date format
    df.index = pd.to_datetime(df.index, format = '%m/%d/%Y').strftime('%m/%d/%Y')

    
    
    #create outputfile using os in the data directory
    output_file = os.path.join(output_directory, f"{ticker}.csv")
    #use pandas to turn our dataframe into a CSV file
    df.to_csv(output_file, header=True)
    
    
    