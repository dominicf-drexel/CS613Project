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
            for i in range(len(self.x_train)):
                # compute the euclidean distance
                distance = np.sqrt(np.sum((x - self.x_train[i]) ** 2))
                target = self.y_train[i]
                distances.append((distance, target))

            # sort the distances
            # need the lambda function because sorting a tuple
            distances.sort(key=lambda x: x[0])
            k_nearest = distances[:self.k]

            # for regression (not classification)
            # get the average of the closest k distances
            targets = []
            for (dist, target) in k_nearest:
                    targets.append(target)
            prediction = np.mean(targets)
            predictions.append(prediction)
        
        return np.array(predictions)
