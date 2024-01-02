tests = {
    "signal": False,
    "d/e": False,
    "pe": False,
    "beta": False,
    "fcf": False,
    "roe": False,
    "peg": False,
    "pb": False,
    "graph": False,
}
import os
import pandas as pd

# Set pandas display options
pd.set_option('display.float_format', '{:.2f}'.format)

def analysis(dirname, folder):
    test = tests.copy()
    stocks = os.listdir(folder)
    indicators = pd.read_csv(os.path.join(dirname, 'Daily_Stock_Report\\Indicators.csv'), index_col='Stocks')

    for i in stocks:
        df = pd.read_csv(os.path.join(folder, i))
        values = indicators.loc[os.path.splitext(i)[0]]
        if vales["beta"] <= 0:
            test["beta"] = True
        if values["priceToBook"] > 1:
            test["pb"] = True
        if 

dirname = os.path.dirname(__file__)
folder = os.path.join(dirname, 'Daily_Stock_Report\\Stocks')
analysis(dirname, folder)