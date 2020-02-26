import requests
import pandas as pd
import csv, json, datetime

from ticker_simpol import get_sp500_symbol

with open('key.json') as config:
    config_data = json.load(config)
    apiKey = config_data['alphavantage-apiKey']
    save_path = config_data['saving-directory']

sp500_symbols = get_sp500_symbol()

for symbol in sp500_symbols:
    res = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={apiKey}')

    df = pd.DataFrame(res.json()['Time Series (5min)'])
    df.transpose().to_csv(f'{save_path}/{symbol}-{datetime.date.today()}.csv')