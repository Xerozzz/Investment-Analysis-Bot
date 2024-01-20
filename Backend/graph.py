import pandas as pd
import matplotlib.pyplot as plt
import os

dirname = os.path.dirname(__file__)
df = pd.read_csv(os.path.join(dirname, "Daily_Stock_Report\\Stocks\\NVDA.csv"))
df[["Close"]].plot()
plt.savefig(os.path.join(dirname, "Daily_Stock_Report\\Graphs\\NVDA.png"))
