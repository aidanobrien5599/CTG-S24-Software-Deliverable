Usage

To run the backtesting strategy, execute the following command in the terminal:
- python3 backtest.py factor_file.csv data_folder


The backtesting strategy involves the following steps:

- Initialization: The script initializes a BacktestStrategy object with the paths to the factor CSV file and the folder containing stock data.\
- Calculating Returns: For each day in the factor data, the script identifies the top 5 
performing stocks based on the factors. It then calculates the daily returns for both the top 5 portfolio and the even portfolio (investing equally in all 25 stocks).
- Plotting Results: Finally, the script plots the cumulative returns of both portfolios over time.-


The script generates a plot showing the cumulative returns of two investment strategies:

Top 5: Investing in the top 5 performing stocks based on the provided factors.
Even: Investing equally across all 25 stocks.