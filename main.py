import TradingENV
import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\Acer\PycharmProjects\RF_Trading\datafile\BNBBUSD1.csv', index_col=0)
env = TradingENV.Environment(df, window=60)
print(np.random.choice(env.action_space))
print(env.current_step)

print(df.loc[env.current_step])

