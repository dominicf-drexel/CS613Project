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

# check the range of sleep time
print(f"Sleep Time min = {np.min(y)}")
print(f"Sleep Time mean = {np.mean(y)}")
print(f"Sleep Time max = {np.max(y)}")
print(f"Sleep Time std = {np.std(y)}")

# check the range of the feature variables
#i = 0
#for col in xcolumnnames:
#    col_values = x[:, i]
#    col_min = np.min(col_values)
#    col_max = np.max(col_values)
#    print(f"col: Min= {str(col_min)} Max= {str(col_max)}")
#    i += 1

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
# gets statistics for all k_values but only the last k_value is used for ensemble
k_values = [int(np.sqrt(trainingdata.shape[0]))]
for k in k_values:
    knn = KNN.KNN(trainingdata, trainingresults, k=k)
    knn_predictions = knn.predict(validationdata)

    # statistics
    knn_mse = Statistics.ComputeMSE(validationresults, knn_predictions)
    knn_rmse = Statistics.ComputeRMSE(validationresults, knn_predictions)
    knn_mae = Statistics.ComputeMAE(validationresults, knn_predictions)
    knn_r2 = Statistics.ComputeR2(validationresults, knn_predictions)
    print(f"KNN k={k} MSE: {knn_mse}")
    print(f"KNN k={k} RMSE: {knn_rmse}")
    print(f"KNN k={k} MAE: {knn_mae}")
    print(f"KNN k={k} R2: {knn_r2}")


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
    

