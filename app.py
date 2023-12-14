import yfinance as yf, pandas as pd, shutil, os, time, glob, smtplib, ssl
from get_all_tickers import get_tickers as gt

from erase import erase
from getData import getData
from getStats import getStats
from sendEmail import sendEmail

# Set Up
dirname = os.path.dirname(__file__)
folder = os.path.join(dirname, 'Daily_Stock_Report\\Stocks')
stocks = ["GOOG", "AMZN", "NVDA"]

# Removes old Stock Folder and recreates it to remove old stocks
erase(folder)

# Get Stock Data
getData(stocks, dirname)

# Perform OBV Analysis
# getStats(folder, dirname)

# Send email report to your gmail
# sendEmail(dirname)

