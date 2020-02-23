import csv

def get_sp500_symbol():
    symbols_csv = []
    symbols = []
    with open("data/sp500.csv") as f:
        reader = csv.reader(f)
        next(reader, None)  # skip the headers

        for row in reader:
            if (row[0] != ''):
                symbols.append(row[0])

    #     symbols_csv = list(reader)

    # symbols = symbols_csv.filter(lambda r: r.length > 0)\
    #                         .map(lambda r: r[0])

        # for row in reader:
        #     symbols.append(row[0])

    return symbols
 