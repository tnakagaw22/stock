import requests
import os.path

save_path = '/home/tomo/dev/stock/data'
price_endpoint = "https://finance.yahoo.com/quote/AAPL/history?period1=1424649600&period2=1582416000&interval=1d&filter=history&frequency=1d"

file_name = "test.csv"
saving_file_name = f"{save_path}/{file_name}"
saving_file=open(saving_file_name, "w")
saving_file.write("""Hello my name is ABCD""")
saving_file.close()

print('Download completed')