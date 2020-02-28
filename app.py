import yfinance as yf
import os.path
import json

from ticker_simpol import get_sp500_symbol

with open('key.json') as config:
    config_data = json.load(config)
    save_path = config_data['histories-saving-directory']

sp500_symbols = get_sp500_symbol()

for symbol in sp500_symbols:
    data = yf.Ticker(symbol)
    history = data.history(period="max")
    saving_file_name = f"{save_path}/{symbol}.csv"
    history.to_csv(saving_file_name)



print('Download completed')