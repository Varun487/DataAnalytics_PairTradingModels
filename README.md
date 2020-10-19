# PairTradingModels

## To replicate this repo on your computer

1. Download the storage folder shared to you in google drive
2. Create a DA Project folder
3. Copy the storage folder as is to the newly created project folder
3. cd to that folder and run `git init`, this initalizes the git repository
4. run `git remote add origin "https://github.com/Varun487/DataAnalytics_PairTradingModels"`
5. run `git pull origin master`
6. Create a virtual environment called `venv` with `python3 -m venv venv`
7. Activate the virtual environment with `source venv/bin/activate`
8. In case the virtual environment isn't working, have a look at the documentation here https://docs.python.org/3/library/venv.html
9. run `pip3 install -r requirements.txt`

## Collection

#### STATUS - Completed

Describes the data collected and the scripts used to collect it.

Contains 2 scripts
1. `list_of_nse_companies.py` - To get names and tickers all stocks floating in the stock market as of 3rd September 2020
2. `stock_candle_data_and_volume.py` - To get historical candle stick data of the stock tickers collected from years 2000 - 2020

## Preprocessing

#### STATUS - Yet to be completed

1. Handling Missing Data - Dropping the rows of the datasets which are missing data we can afford to do this due to a large amount of data and interpolation may lead to inaccurate data due to the volatility of some stocks.
2. Deleting datasets which have < 2 months worth of data.
3. Deleting the parts of the datasets with > 2 years of data - as a correlation needs to be within a fixed time period and we cannot let a strong correlation in the past affect the predictions made by the model when there is no significant correlation currently.
4. Adding Company name and Exchange to the datasets for easy identification.
5. Create Bollinger Bands for all stocks - Calculate the 20 Day Moving Average for all companies closing prices allong with the 1, 2, 3 standard deviation prices above and below the company.
6. Creating an interactive visualization for all stocks to see the bollinger bands and stock price data.
7. Create Pairs, calculate correlations, do multiple cointegration tests on the stocks to ensure that the pairs are truly correlated.
8. Create appropriate visualization for the pairs and ensure that they move in tandem visually.

## Models

#### STATUS - Yet to be completed

Currently 2 models, may add more if time permits and after finding more insight from data
1. To calculate spreads, use regression to find the optimal ratio(R) between the pair in the equation `A - R.B = W` where W the Spread must be 0 to ensure the stocks are mean reverting and stationery and A and B are Moving averages of the stock prices of the pair.
2. Visualization of the mean reverting spreads of the moving averages of the pair.
3. Using Spreads, we make a decision tree which decides to *BUY*, *SELL*, or *FLAT* a stock.
4. visualize the various *BUY*/*SELL*/*FLAT* decisions of the Decision tree.

## Back tester

#### STATUS - Yet to be completed

Goes through all the orders made by the decision tree and calculates profit, loss, p&l ratio, Sharpe ratio, etc.. and provides suitable data analysis and visualizations
