# Import libraries
import yfinance as yf
import pandas as pd
import shutil
import os
import time
import glob
import smtplib
import ssl
from get_all_tickers import get_tickers as gt

# Import python files
from getData import getData
# from getStats import getStats
from sendEmail import sendEmail
from analysis import analysis
from pdf import pdf

# Set Up
# Check if stock folder exists, if not create it
if not (os.path.exists("Daily_Stock_Report")):
    os.makedirs("Daily_Stock_Report")
if not (os.path.exists("Daily_Stock_Report\\Stocks")):
    os.makedirs("Daily_Stock_Report\\Stocks")
if not (os.path.exists("Daily_Stock_Report\\Reports")):
    os.makedirs("Daily_Stock_Report\\Reports")

dirname = os.path.dirname(__file__)
folder = os.path.join(dirname, 'Daily_Stock_Report\\Stocks')
stocks = ["GOOG", "AMZN", "NVDA"]

# Get Stock Data
getData(stocks, dirname)

# Perform Analysis
indicators, objects = analysis(dirname, folder)

# Generate Report
pdf(indicators, objects, dirname)

# Send email report to your gmail
sendEmail(dirname)
