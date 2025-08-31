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
filepath: str = "./data/atus_00005.csv"
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

y: np.ndarray = ExtractY(matrixdata, "ACT_PCARE_SLEEP_010101", matrixcolumnnames)
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
# currently statistics are printed directly
# from within the s_folds_validation method
validation_stats, linear_models = LinearRegression.s_folds_validation(trainingdata, trainingresults, 5)
print(f"LR Mean: {validation_stats['mean']}")
print(f"LR STD: {validation_stats['std']}")
print(f"LR ALL RMSE: {validation_stats['all_rmse']}")

# knn regression algorithm
print("START k nearest neighbors: fit")
knn = KNN.KNN(trainingdata, trainingresults, k=5)
print("START k nearest neighbors: predict")
knn_predictions = knn.predict(validationdata)
#print(f"knn predictions shape = {knn_predictions.shape}")
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


# predictions from all linear regression models
# S-fold * runs = number of models
# So if S-fold=5 then 5*100 models
all_lr_predictions = []
for run_models in linear_models: # 20 runs (hardcoded in LinearRegression.py)
    for model in run_models: # 5 (hardcoded in this file)
        lr_pred = model.predict(validationdata)
        all_lr_predictions.append(lr_pred)


# average ALL linear regression predictions and KNN
ensemble_predictions = []
for i in range(len(validationdata)):
    lr_aggregate_prediction = np.mean([pred[i] for pred in all_lr_predictions])
    final_ensemble_prediction = (lr_aggregate_prediction + knn_predictions[i]) / 2
    ensemble_predictions.append(final_ensemble_prediction)

ensemble_predictions = np.array(ensemble_predictions)

print(f"ensemble_predictions = {ensemble_predictions}")
ensemble_mse = Statistics.ComputeMSE(validationresults, ensemble_predictions)
ensemble_rmse = Statistics.ComputeRMSE(validationresults, ensemble_predictions)
print(f"Ensemble MSE: {ensemble_mse}")
print(f"Ensemble RMSE: {ensemble_rmse}")
    

