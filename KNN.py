import numpy as np

class KNN:
    def __init__(self, k: int = 5):
        self.k = k

    def train(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train

    def predict(self, x_test):
        predictions = []
        return np.array(predictions)
