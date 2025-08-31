import numpy as np

#filepath: str = "./data/atus_00003.csv"
#(rowsdata, columnnames) = LoadATUSExtract(filepath)
#
#(readyrows, readycolumns) = TransformIntoFeatures(rowsdata, columnnames)
#
#(matrixdata, matrixcolumnnames) = RowsToMatrix(readyrows, readycolumns)
#
#x: np.ndarray = ExtractX(matrixdata, matrixcolumnnames, True)
#bias_column = np.ones((x.shape[0],1))
#
##BLS_PCARE_SLEEP is not in the dataset given, change "ACT_PCARE" to BLS_PCARE_SLEEP
#y: np.ndarray = ExtractY(matrixdata, "ACT_PCARE", matrixcolumnnames)
#y_reshaped = y.reshape(-1, 1)
#
#data = np.concatenate((bias_column, x, y_reshaped), axis=1)

class LinearRegressionGradient:
    def __init__(self, learn_rate=0.01, epochs=1000):
        self.weights = None
        self.learn_rate = learn_rate
        self.epochs = epochs

    def preprocess(self, trainingdata, trainingresults, validationdata, validationresults):
        y_train = trainingresults
        y_train = y_train.reshape(-1, 1)
        y_val = validationresults
        y_val = y_val.reshape(-1, 1)

        mean = np.atleast_2d(np.mean(trainingdata, axis=0))

        std = np.atleast_2d(np.std(trainingdata, axis=0, ddof=1))
        std[std == 0] = 1

        z_scored_data_train = (trainingdata - mean) / std
        bias_train = np.ones((len(trainingdata),1))
        x_train = np.column_stack([bias_train, z_scored_data_train])

        z_scored_data_val = (validationdata - mean) / std
        bias_val = np.ones((len(validationdata),1))
        x_val = np.column_stack([bias_val, z_scored_data_val])

        return x_train, y_train, x_val, y_val


    def fit(self, x_train, y_train, x_val):
        self.weights = np.random.uniform(-0.0001, 0.0001, size=(len(x_train[0]),1))

        N = len(x_train)

        for i in range(self.epochs):
            y_hat_train = x_train @ self.weights
            gradient = (2/N)*(np.transpose(x_train))@(y_hat_train - y_train)
            self.weights = self.weights - (self.learn_rate*gradient)

        y_hat_val = x_val @ self.weights
        return y_hat_train, y_hat_val
    
    def predict(self, x):
        predictions = x @ self.weights
        return predictions
    
    
def gradient_batch_regression(trainingdata, trainingresults, validationdata, validationresults, learn_rate=0.01, epochs=1000):
    lr = LinearRegressionGradient(learn_rate=learn_rate, epochs=epochs)
    x_train, y_train, x_val, y_val = lr.preprocess(trainingdata, trainingresults, validationdata, validationresults)

    # Batch training
    lr.fit(x_train, y_train, x_val)

    y_hat_train = lr.predict(x_train)
    y_hat_val = lr.predict(x_val)

    rmse_train = np.sqrt(np.mean((y_train - y_hat_train)**2))
    rmse_val = np.sqrt(np.mean((y_val - y_hat_val)**2))

    difference_train = np.abs(y_train - y_hat_train)
    sum_train = np.abs(y_train) + np.abs(y_hat_train)
    smape_train = np.mean(difference_train / sum_train)

    difference_val = np.abs(y_val - y_hat_val)
    sum_val = np.abs(y_val) + np.abs(y_hat_val)
    smape_val = np.mean(difference_val / sum_val)

    print("\nBatch Gradient Descent Evaluation:")
    print("Training RMSE: ", rmse_train)
    print("Validation RMSE: ", rmse_val)
    print("Training SMAPE: ", smape_train)
    print("Validation SMAPE: ", smape_val)