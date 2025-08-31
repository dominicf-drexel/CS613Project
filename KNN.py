import numpy as np

class KNN:
    def __init__(self, x_train, y_train, k: int = 5):
        self.k = k

        # normalization parameters
        self.mean = np.mean(x_train, axis=0)
        self.std = np.std(x_train, axis=0)

        # prevent div by 0
        #if self.std == 0:
        #    self.std = 1
        self.std[self.std == 0] = 1

        # normalize training data
        self.x_train = (x_train - self.mean) / self.std # features
        self.y_train = y_train # labels / targets of features

    def predict(self, x_test):

        x_test_normalized = (x_test - self.mean) / self.std
        
        predictions = []

        j = 0
        for x in x_test_normalized:
            j += 1
            if j % 100 == 0:
                print(f"{j} of {len(x_test_normalized)}")
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
