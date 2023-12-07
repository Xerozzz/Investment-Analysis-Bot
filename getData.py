import yfinance as yf, pandas as pd, shutil, os, time, glob, smtplib, ssl
from get_all_tickers import get_tickers as gt

def getData(stocks):
    # Data Holders
    API_Calls = 0 # Holds amount of API calls made
    Stock_Failure = 0  # Used to make sure we don't waste too many API calls on one Stock ticker that could be having issues
    Stocks_Not_Imported = 0
    Failed_Stocks = []

    # Iterate through stocks and retrieve data
    i = 0
    while (i < len(stocks)) and (API_Calls < 1800):
        try:
            stock = yf.Ticker(stocks[i])
            Hist_data = stock.history(period="max")
            print(Hist_data)
            Hist_data.to_csv(".\\Daily_Stock_Report\\Stocks\\" + stocks[i] + ".csv")
            time.sleep(2) # Sleep for 2 seconds to not overload API
            API_Calls += 1
            Stock_Failure = 0
            i += 1
        except ValueError:
            print("Yahoo finance backend error")
            if Stock_Failure > 5: # Move on to next stock after 5 failures
                i += 1
                Stocks_Not_Imported += 1
            API_Calls += 1
            Stock_Failure += 1
            Failed_Stocks.append(stocks[i])
    print("The amount of stocks we successfully imported: " + str(i - Stocks_Not_Imported))
    if Stocks_Not_Imported > 0:
        print("The amount of stocks we failed to import: " + str(Stocks_Not_Imported))
        print("These stocks failed to import: " + str(Failed_Stocks))
    else:
        print("All stocks were successfully imported")