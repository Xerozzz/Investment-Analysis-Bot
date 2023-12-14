import pandas as pd, shutil, os, time, glob, smtplib, ssl

def getStats(folder, dirname):
    path = os.path.join(folder, '*.csv')

def obv(folder, dirname):
    # OBV Analysis Example
    path = os.path.join(folder, '*.csv')
    list_files = (glob.glob(path)) # Get list of CSV Files
    obv_data = [] 
    interval = 0
    while interval < len(list_files):
        df = pd.read_csv(list_files[interval])
        increase = []
        decrease = []
        OBV_value = 0
        count = 0
        while count < 10:
            if df.iloc[count, 1] < df.iloc[count, 4]: # True if stock increased in price
                increase.append(count)
            elif df.iloc[count, 1] > df.iloc[count, 4]: # True if stock decreased in price
                decrease.append(count)
            count += 1
        count2 = 0
        for i in increase:
            OBV_value = round(OBV_value + (df.iloc[i,5]/df.iloc[i,1]))
        for i in decrease:
            OBV_value = round(OBV_value - (df.iloc[i,5]/df.iloc[i,1]))
        current_stock_name = ((os.path.basename(list_files[interval])).split(".csv")[0])
        obv_data.append([current_stock_name, OBV_value])
        interval += 1
    df2 = pd.DataFrame(obv_data, columns = ['Stock', 'OBV_Value'])
    df2["Stocks_Ranked"] = df2["OBV_Value"].rank(ascending=False)
    df2.sort_values(by=['OBV_Value'], inplace=True, ascending=False)
    df2.to_csv(os.path.join(dirname, 'Daily_Stock_Report\\OBV_Ranked.csv'), index=False)