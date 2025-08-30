import numpy as np
from DataLoad import LoadATUSExtract
from CreateFeatures import TransformIntoFeatures
from MatrixCreation import RowsToMatrix, ExtractX, ExtractY

filepath: str = "./data/atus_00003.csv"
(rowsdata, columnnames) = LoadATUSExtract(filepath)

(readyrows, readycolumns) = TransformIntoFeatures(rowsdata, columnnames)

(matrixdata, matrixcolumnnames) = RowsToMatrix(readyrows, readycolumns)

x: np.ndarray = ExtractX(matrixdata, matrixcolumnnames, True)
bias_column = np.ones((x.shape[0],1))

#BLS_PCARE_SLEEP is not in the dataset given, change "ACT_PCARE" to BLS_PCARE_SLEEP
y: np.ndarray = ExtractY(matrixdata, "ACT_PCARE", matrixcolumnnames)
y_reshaped = y.reshape(-1, 1)

data = np.concatenate((bias_column, x, y_reshaped), axis=1)

np.random.seed(0)
np.random.shuffle(data)

datasets = np.array_split(data, 3, axis=0)

training_set = np.concatenate((datasets[0],datasets[1]))
validation_set = datasets[2]

y_train = training_set[:, -1]
y_train = y_train.reshape(-1, 1)
y_val = validation_set[:, -1]
y_val = y_val.reshape(-1, 1)

mean = np.atleast_2d(np.mean(training_set[:, :-1], axis=0))

std = np.atleast_2d(np.std(training_set[:, :-1], axis=0, ddof=1))
std[std == 0] = 1

z_scored_data_train = (training_set[:, :-1] - mean) / std
bias_train = np.ones((len(training_set),1))
x_train = np.column_stack([bias_train, z_scored_data_train])

z_scored_data_val = (validation_set[:, :-1] - mean) / std
bias_val = np.ones((len(validation_set),1))
x_val = np.column_stack([bias_val, z_scored_data_val])

weights = np.random.uniform(-0.0001, 0.0001, size=(len(x_train[0]),1))

learn_rate = 0.01
N = len(x_train)

for i in range(10000):
    y_hat_train = x_train @ weights
    y_hat_val = x_val @ weights

    gradient = (2/N)*(np.transpose(x_train))@(y_hat_train - y_train)

    weights = weights - (learn_rate*gradient)

rmse_train = np.sqrt(np.mean((y_train - y_hat_train)**2))
rmse_val = np.sqrt(np.mean((y_val - y_hat_val)**2))

difference_train = np.abs(y_train - y_hat_train)
sum_train = np.abs(y_train) + np.abs(y_hat_train)
smape_train = np.mean(difference_train / sum_train)

difference_val = np.abs(y_val - y_hat_val)
sum_val = np.abs(y_val) + np.abs(y_hat_val)
smape_val = np.mean(difference_val / sum_val)

print("Training RMSE: ", rmse_train)
print("Validation RMSE: ", rmse_val)
print("Training SMAPE: ", smape_train)
print("Validation SMAPE: ", smape_val)