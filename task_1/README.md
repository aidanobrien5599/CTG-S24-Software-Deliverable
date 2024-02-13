
How to run/access the data
- Run the data_collection.py file to access the data
- The yfinance API provided overall complete data to begin with, but a forward fill method was applied to ensure there were no missing data points
- Every csv file has the same structure and same number of entries

Interpreting the data:

Each CSV file contains historical stock data for one of the top 25 weighted stocks over a three-year period. Each row in the file represents one trading day, and the columns contain the following data points:

Date: The date of the trading day.
Open: The opening price of the stock on that trading day.
High: The highest price the stock reached during the trading day.
Low: The lowest price the stock reached during the trading day.
Close: The closing price of the stock on that trading day.
Adj Close: The adjusted closing price of the stock on that trading day.
Volume: The volume of shares traded on that trading day.