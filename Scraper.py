from binance.client import Client
import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

client = Client(api_key='lafru5jzmsppqsiabFWlNCzGxHdn6WtD6VfEeKX572RmVkGdl0OvS6T2d6iEbdk1',
                api_secret='WCCIdjzMhFuxOWiAQz19Lv4ntjInQ9QmShc8ZL8iMHY9kjNMGlbjRU4RbdaeKJr5')

pair = os.getenv('PAIR', 'BNBBUSD')
since = os.getenv('SINCE', '2 year ago UTC')
df = client.get_historical_klines(symbol=pair, interval=Client.KLINE_INTERVAL_1MINUTE, start_str=since)

real_values = []

for row in df:
    real_values.append([row[1], row[4]])

real_df = pd.DataFrame(real_values, columns=['Open_price', 'Close_price'])

normalizer = StandardScaler()
normalizer.fit(df)
df = normalizer.transform(df)
df = pd.DataFrame(df, columns=[
    'Open time', 'Open', 'High', 'Low', 'Close', 'Volume',
    'Close time', 'Quote asset volume', 'Number of trades',
    'Taker buy base asset volume',
    'Taker buy quote asset volume', 'Ignore'
    ])

df.drop(['Open time', 'Close time', 'Ignore'], axis=1, inplace=True)
df.plot()

df = pd.concat([df, real_df], axis=1)
df = df[:-1]

print(df.head())
print(df.tail())

df.to_csv('C:/Users/Acer/PycharmProjects/Binance_Trading_Bot/datafile/BNBBUSD1.csv')
plt.show()
