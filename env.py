import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns


class Environment:

    def __init__(self, df, window, min_performance=0.65, start=0, end=None, initial_balance=1000):
        self.df = df
        self.window = window
        self.min_performance = min_performance
        self.start = start
        self.end = end
        self.total_steps = len(self.df)
        self.initial_balance = initial_balance
        self.min_account_balance = 0
        self.min_transaction_value = 10
        self.total_fee = 0

        self.action_space = np.arange(0, 1, 0.01)
        self.observation_space = np.arange(0, self.window)

    def reset(self):
        self.balance = initial_balance
        self.performance = performance



