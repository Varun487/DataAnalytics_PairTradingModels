# Pair Trading Models

## To replicate this repo on your computer

1. Download the storage folder shared to you in google drive.
2. Create a DA Project folder
3. Copy the storage folder as is to the newly created project folder
3. cd to that folder and run `git init`, this initializes the git repository
4. run `git remote add origin "https://github.com/Varun487/DataAnalytics_PairTradingModels"`
5. run `git pull origin master`
6. Create a virtual environment called `venv` with `python3 -m venv venv`
7. Activate the virtual environment with `source venv/bin/activate`
8. In case the virtual environment isn't working, have a look at the documentation here https://docs.python.org/3/library/venv.html
9. run `pip3 install -r requirements.txt`

## Collection

#### STATUS - Completed

###### Describes the data collected and the scripts used to collect it.

Contains 2 scripts
1. `list_of_nse_companies.py` - To get names and tickers all stocks floating in the stock market as of 3rd September 2020
2. `stock_candle_data_and_volume.py` - To get historical candle stick data of the stock tickers collected from years 2000 - 2020

## Preprocessing

###### Clean data + Find 5 top stock pairs (2 pairs per sector) of the stock market to trade and perform correlation and co-integration testing.

#### STATUS - Completed for 0/5 pairs

1. Handling Missing Data - Dropping the rows of the datasets which are missing data we can afford to do this due to a large amount of data and interpolation may lead to inaccurate data due to the volatility of some stocks.
2. Deleting datasets which have < 3 years worth of data.
3. Deleting the parts of the datasets with > 3 years of data (taking only data in range of years 2017-2019) - as a correlation needs to be within a fixed time period and we cannot let a strong correlation in the past affect the predictions made by the model when there is no significant correlation currently.
4. Adding Company name and Exchange to the datasets for easy identification.
5. Choose and find 10 stock pairs and the periods in which they are highly correlated and co-integrated.
6. Create Bollinger Bands for chosen stocks to help aid visualization - Calculate the 20 Day Moving Average for all companies closing prices along with the 1, 2, 3 standard deviation prices above and below the share price.
7. Show that visually the shares in a particular pair move in tandem.
8. Perform pair trading and generate orders for these 5 stock pairs according to z-score.
9. Also add appropriate visualizations to the creation of orders.

## Models

###### Create ML models for all chosen stocks and predict values for the decided prediction week for each pair

#### STATUS - Completed for 0/5 pairs

1. Decide the week of prediction for all pairs.
2. For each stock, generate 4 models
    * Linear Regression
    * ARIMA
    * SARIMA
    * LSTM
3. For each model try to adjust it's parameters and training data for it to best fit the actual data of the test week for the stock pair.
4. Get predictions for all stocks and all models per stocks.

## Back tester

###### Calculate returns given trading parameters, orders and real data for week and predicted data from models. Helps to evaluate different models and give the best model per stock.

#### STATUS - Completed for 0/5 pairs

1. Decide capital, risk, rules for opening and closing a trade and other parameters for trading and trading style.
2. Run the orders on all stocks real data for prediction week and models' predicted data.
3. Calculate ratios and other parameters for all models' predicted values and evaluate them for each stock.
4. Find best model per stock to maximize profit and establish whether pair trading is feasible with ML models.

