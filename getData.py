import yfinance as yf
import pandas as pd
import shutil
import os
import time
import glob
import smtplib
import ssl
from get_all_tickers import get_tickers as gt


def getData(stocks, dirname):
    # Data Holders
    API_Calls = 0  # Holds amount of API calls made
    Stock_Failure = 0  # Used to make sure we don't waste too many API calls on one Stock ticker that could be having issues
    Stocks_Not_Imported = 0
    Failed_Stocks = []

    # Iterate through stocks and retrieve data
    i = 0
    data = {
        "previousClose": [],
        "open": [],
        "dayLow": [],
        "dayHigh": [],
        "volume": [],
        "trailingPE": [],
        "beta": [],
        "priceToBook": [],
        "pegRatio": [],
        "debtToEquity": [],
        "returnOnEquity": [],
        "freeCashflow": [],
    }

    while (i < len(stocks)) and (API_Calls < 1800):
        try:
            stock = yf.Ticker(stocks[i])

            # Store stock historical data
            historical_data = stock.history(period="1mo")
            historical_data.to_csv(os.path.join(
                dirname, 'Daily_Stock_Report\\Stocks\\' + stocks[i] + '.csv'))

            # Store stock indicators data
            stock_data = stock.info
            data["previousClose"].append(stock_data["previousClose"])
            data["open"].append(stock_data["open"])
            data["dayLow"].append(stock_data["dayLow"])
            data["dayHigh"].append(stock_data["dayHigh"])
            data["volume"].append(stock_data["volume"])
            data["trailingPE"].append(stock_data["trailingPE"])
            data["beta"].append(stock_data["beta"])
            data["priceToBook"].append(stock_data["priceToBook"])
            data["pegRatio"].append(stock_data["pegRatio"])
            data["debtToEquity"].append(stock_data["debtToEquity"])
            data["returnOnEquity"].append(stock_data["returnOnEquity"])
            data["freeCashflow"].append(stock_data["freeCashflow"])

            time.sleep(2)  # Sleep for 2 seconds to not overload API
            API_Calls += 1
            Stock_Failure = 0
            i += 1
        except ValueError:
            print("Yahoo finance backend error")
            if Stock_Failure > 5:  # Move on to next stock after 5 failures
                i += 1
                Stocks_Not_Imported += 1
            API_Calls += 1
            Stock_Failure += 1
            Failed_Stocks.append(stocks[i])
            stocks.pop(i)
    df = pd.DataFrame(data, index=stocks)
    df.to_csv(os.path.join(dirname, 'Daily_Stock_Report\\Indicators.csv'))
    print("The amount of stocks we successfully imported: " +
          str(i - Stocks_Not_Imported))
    if Stocks_Not_Imported > 0:
        print("The amount of stocks we failed to import: " +
              str(Stocks_Not_Imported))
        print("These stocks failed to import: " + str(Failed_Stocks))
    else:
        print("All stocks were successfully imported")
