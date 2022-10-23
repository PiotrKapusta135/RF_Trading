

class Agent:
    def __init__ (self, hidden_units, learning_rate, train_env, test_env):
        self.train_env = train_env
        self.test_env = test_env
        self.hidden_units = hidden_units
        self.epsilon = 1
        self.min_epsilon = 0.1
        self.epsilon_decay = 0.02
        self.learning_rate = learning_rate
        self.gamma = 0.95
        self.batch_size = 126
        self.model = self.build_model(hidden_units, learning_rate)


    def build_model(self, hu, lr):
        model = Sequential()
        model.add(Dense(hu, input_shape=(self.train_env.window, len(self.train_env.df.columns))))

