import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns


class Environment:

    def __init__(self, df, window, features, min_performance, start=0, end=None, mu=None, std=None):
        self.df = df
        self.window = window
        self. features = features
        self.min_performance = min_performance
        self.start = start
        self.end = end
        self.mu = mu
        self.std = std
