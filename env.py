import pandas as pd
import numpy as np
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
        self.balance = initial_balance
        self.prev_balance = 0
        self.action_result = initial_balance - balance
        self.min_account_balance = 0
        self.min_transaction_value = 10
        self.total_fee = 0
        self.trades_made = 0
        self.account_history = deque(maxlen=self.window)
        self.market_history = deque(maxlen=self.window)
        self.performance = 1

        self.action_space = np.arange(0, 1, 0.01)
        self.observation_space = np.arange(0, self.window)

    def reset(self):
        self.balance = initial_balance
        self.performance = 1
        self.total_fee = 0
        self.prev_balance = initial_balance
        self.action_result = 0
        self.trades_made = 0
        self.starting_step = random.randint(0, len(self.df.loc[:].values - self.window))
        self.current_step = self.starting_step
        for i in reversed(range(self.window)):
            self.current_step = self.current_step - 1
            self.account_history.append([self.balance, self.total_fee, self.trades_made])
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

    #def step(self):





