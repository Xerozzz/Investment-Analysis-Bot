import pandas as pd
import os

tests = {
    "signal": "Healthy",
    "d/e": "Healthy",
    "beta": "Healthy",
    "roe": "Healthy",
    "peg": "Healthy",
    "pb": "Healthy",
    "graph": "Healthy",
}

objects = {

}


# Set pandas display options
pd.set_option('display.float_format', '{:.2f}'.format)


def analysis(dirname, folder):
    stocks = os.listdir(folder)
    indicators = pd.read_csv(os.path.join(
        dirname, 'Daily_Stock_Report\\Indicators.csv'), index_col='Stocks')

    for i in stocks:
        test = tests.copy()
        stock = os.path.splitext(i)[0]
        df = pd.read_csv(os.path.join(folder, i))
        values = indicators.loc[stock]

        prev = df.iloc[-2].tolist()[4]
        current = df.iloc[-1].tolist()[4]

        if prev > current:
            test["signal"] = "ALERT"
        if values["beta"] <= 0:
            test["beta"] = "ALERT"
        if values["priceToBook"] > 1:
            test["pb"] = "ALERT"
        if values["pegRatio"] > 1:
            test["peg"] = "ALERT"
        if values["debtToEquity"] > 1:
            test["d/e"] = "ALERT"
        if values["returnOnEquity"] < 0.1:
            test["roe"] = "ALERT"
        objects[stock] = test

    return indicators, objects
