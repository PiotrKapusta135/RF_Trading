import pandas as pd
import numpy as np
import random
from collections import deque

import matplotlib.pyplot as plt
import seaborn as sns


class Environment:

    def __init__(self, df, window, min_performance=0.65, initial_balance=1000):
        self.df = df
        self.window = window
        self.min_performance = min_performance
        self.total_steps = len(self.df)
        self.initial_balance = initial_balance
        self.usd_balance = initial_balance
        self.crypto_balance = 0
        self.net_worth = initial_balance
        self.min_account_balance = 0
        self.min_transaction_value = 10
        self.total_fee = 0
        self.trades_made = 0
        self.account_history = deque(maxlen=self.window)
        self.market_history = deque(maxlen=self.window)
        self.performance = 1
        self.crypto_bought = 0
        self.crypto_sold = 0
        self.crypto_held = 0
        self.trading_fee = 0.05

        self.action_space = np.arange(0, 1, 0.01)
        self.observation_space = np.arange(0, self.window)

    def reset(self):
        self.usd_balance = initial_balance
        self.crypto_balance = 0
        self.performance = 1
        self.total_fee = 0
        self.net_worth = initial_balance
        self.trades_made = 0
        self.max_net_worth = self.net_worth
        self.starting_step = random.randint(0, len(self.df.loc[:].values - self.window))
        self.current_step = self.starting_step
        for i in reversed(range(self.window)):
            self.current_step = self.current_step - 1
            self.account_history.append([self.usd_balance, self.crypto_balance, self.total_fee, self.trades_made,
                                         self.crypto_bought, self.crypto_sold, self.crypto_held])
            self.market_history.append([self.df.loc[self.current_step, 'Open'],
                                        self.df.loc[self.current_step, 'High'],
                                        self.df.loc[self.current_step, 'Low'],
                                        self.df.loc[self.current_step, 'Close'],
                                        self.df.loc[self.current_step, 'Volume']])
        state = np.concatenate((self.market_history, self.account_history), axis=1)
        return state

    def get_state(self):
        self.market_history.append([self.df.loc[self.current_step, 'Open'],
                                    self.df.loc[self.current_step, 'High'],
                                    self.df.loc[self.current_step, 'Low'],
                                    self.df.loc[self.current_step, 'Close'],
                                    self.df.loc[self.current_step, 'Volume']])
        obs = np.concatenate((self.market_history, self.account_history), axis=1)
        return obs

    def step(self, action):
        self.current_price = random.uniform(self.df.loc[self.current_step, 'Open'],
                                             self.df.loc[self.current_step, 'Close'])
        self.max_net_worth = self.usd_balance + self.crypto_balance
        if action == 0:
            self.crypto_held = self.crypto_held + 1
            pass
        elif action > 0:
            self.crypto_bought = self.usd_balance * action / self.current_price
            self.crypto_balance = self.crypto_balance + self.crypto_bought
            self.usd_balance = self.usd_balance - (self.crypto_bought * self.current_price +
                                                   self.crypto_bought * self.current_price * self.trading_fee)
            self.total_fee = self.total_fee + self.crypto_bought * self.current_price * self.trading_fee
        elif action < 0:
            self.crypto_sold = self.crypto_balance * action
            self.crypto_balance = self.crypto_balance - self.crypto_bought
            self.usd_balance = self.usd_balance + (self.crypto_sold * self.current_price -
                                                   self.crypto_sold * self.current_price * self.trading_fee)
            self.total_fee = self.total_fee + self.crypto_sold * self.current_price * self.trading_fee

        self.net_worth = self.usd_balance + self.crypto_balance
        if self.net_worth > self.max_net_worth:
            self.max_net_worth = self.net_worth
            # Reward + 1?



