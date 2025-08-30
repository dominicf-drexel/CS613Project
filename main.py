import numpy as np
from DataLoad import LoadATUSExtract
from CreateFeatures import TransformIntoFeatures
from MatrixCreation import RowsToMatrix, ExtractX, ExtractY
from DataOperations import GenerateTrainingValidationIndices, GenerateTrainingValidationIndicesByFeatureValue, GetSubset
import LinearRegression
import KNN
import Statistics

#
#Load data:
filepath: str = "./data/atus_00003.csv"
(rowsdata, columnnames) = LoadATUSExtract(filepath)
#print(columnnames)

(readyrows, readycolumns) = TransformIntoFeatures(rowsdata, columnnames)
#print(readycolumns)

(matrixdata, matrixcolumnnames) = RowsToMatrix(readyrows, readycolumns)
#print(matrixcolumnnames)

#Create Training, Validation data:
x: np.ndarray
xcolumnnames: list[str]
x, xcolumnnames = ExtractX(matrixdata, matrixcolumnnames, True)
print(f"x.shape={x.shape}")

y: np.ndarray = ExtractY(matrixdata, "ACT_WORK", matrixcolumnnames)
print(f"y.shape={y.shape}")
#print(y)

# (trainingindices, validationindices) = GenerateTrainingValidationIndices(x, 0)
(trainingindices, validationindices) = GenerateTrainingValidationIndicesByFeatureValue(x, 0, matrixcolumnnames, "YEAR")
(trainingdata, trainingresults) = GetSubset(x, y, trainingindices)
(validationdata, validationresults) = GetSubset(x, y, validationindices)

print(f"training data = {trainingdata.shape}")
print(f"training results = {trainingresults.shape}")
print(f"validation data = {validationdata.shape}")
print(f"validation results = {validationresults.shape}")

#Analysis:

# linear regression algorithm
#lr = LinearRegression()
#print("START linear regression: fit")
#lr.fit(trainingdata, trainingresults)
#print("START linear regression: predict")
#linear_predictions = lr.predict(validationdata)
#print(f"linear predictions shape = {linear_predictions.shape}")
# linear regression evaluation
LinearRegression.s_folds_validation(trainingdata, trainingresults, 5)

# knn regression algorithm
print("START k nearest neighbors: fit")
knn = KNN.KNN(trainingdata, trainingresults, k=5)
print("START k nearest neighbors: predict")
knn_predictions = knn.predict(validationdata)
print(f"knn predictions shape = {knn_predictions.shape}")
# knn regression evalation
#knn_mse = np.mean((validationresults - knn_predictions) ** 2)
knn_mse = Statistics.ComputeMSE(validationresults, knn_predictions)
knn_rmse = Statistics.ComputeRMSE(validationresults, knn_predictions)
knn_mae = Statistics.ComputeMAE(validationresults, knn_predictions)
knn_r2 = Statistics.ComputeR2(validationresults, knn_predictions)
print(f"KNN MSE: {knn_mse}")
print(f"KNN RMSE: {knn_rmse}")
print(f"KNN MAE: {knn_mae}")
print(f"KNN R2: {knn_r2}")


# ensemble algorithm consists of the following models
# s-fold linear regression models
# 1 KNN model

"""
ensemble_predictions = []
x_test = []
for i in range(len(x_test)):
    predictions = []

    # add the linear regression predictions
    for pred in linear_predictions:
        predictions.append(pred[i])

    # add the knn regression predictions
    predictions.append(knn_predictions[i])
    
    # ensemble algorithm
"""
    

