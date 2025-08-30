import numpy as np

class KNN:
    def __init__(self, x_train, y_train, k: int = 5):
        self.k = k

        # training data
        self.x_train = x_train # features
        self.y_train = y_train # labels / targets of features



    def predict(self, x_test):
        predictions = []

        for x in x_test:
            distances = []
            #for (feature, target) in (self.x_train, self.y_train):
            for i in range(len(self.x_train)):
                # compute distance
                distance = 0
                target = self.y_train[i]
                distances.append((distance, target))

            # sort the distances

            # for regression (not classification)
            # get the average of the closest k distances
            prediction = distances[0]
            predictions.append(prediction)
        
        return np.array(predictions)
