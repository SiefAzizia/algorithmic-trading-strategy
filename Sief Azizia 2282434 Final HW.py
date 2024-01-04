# Task 1: Load data from orcl.csv into a list of dictionaries

data = []

with open(r''
          # 'path here'
 ,'r') as file:
    header = file.readline().strip().split(',')

    for line in file:
        values = line.strip().split(',')

        record = {header[i]: values[i] for i in range(len(header))}

        data.append(record)

# Task 2: Calculate Simple Moving Averages and Relative Strength Index

for i in range(4, len(data)):
    sum_close = sum(float(data[j]['Close']) for j in range(i - 4, i + 1))

    data[i]['SMA_5'] = sum_close / 5

for i in range(14, len(data)):

    avg_gain = 0

    avg_loss = 0

    for j in range(i - 13, i):

        change = float(data[j]['Close']) - float(data[j - 1]['Close'])

        if change > 0:

            avg_gain += change

        else:

            avg_loss += abs(change)

    avg_gain /= 14

    avg_loss /= 14

    if avg_loss != 0:

        rs = avg_gain / avg_loss

        rsi = 100 - (100 / (1 + rs))

    else:

        rsi = 100

    data[i]['RSI_14'] = rsi

# Task 3: Write indicators to separate CSV files

with open('orcl-sma.csv', 'w') as sma_file:
    sma_file.write('Date,SMA_5\n')

    for i in range(4, len(data)):
        sma_file.write(f"{data[i]['Date']},{data[i]['SMA_5']}\n")

with open('orcl-rsi.csv', 'w') as rsi_file:
    rsi_file.write('Date,RSI_14\n')

    for i in range(14, len(data)):
        rsi_file.write(f"{data[i]['Date']},{data[i]['RSI_14']}\n")