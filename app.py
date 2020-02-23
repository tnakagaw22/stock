import yfinance as yf
import os.path

from ticker_simpol import get_sp500_symbol

save_path = '/home/tomo/dev/stock/data/histories'
sp500_symbols = get_sp500_symbol()

for symbol in sp500_symbols:
    data = yf.Ticker(symbol)
    history = data.history(period="max")
    saving_file_name = f"{save_path}/{symbol}.csv"
    history.to_csv(saving_file_name)



print('Download completed')