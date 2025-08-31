import numpy as np
from DataLoad import LoadATUSExtract
from CreateFeatures import TransformIntoFeatures
from MatrixCreation import RowsToMatrix, ExtractX, ExtractY
from DataOperations import GenerateTrainingValidationIndices, GenerateTrainingValidationIndicesByFeatureValue, GetSubset
import LinearRegression
import LinearRegressionGradient
import KNN
import Statistics
import pickle


#Load data:
filepath: str = "./data/atus_00006.csv"
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
#print(f"x.shape={x.shape}")

y: np.ndarray = ExtractY(matrixdata, "ACT_PCARE_SLEEP_010101", matrixcolumnnames)
# ... rest of your code


y: np.ndarray = ExtractY(matrixdata, "ACT_PCARE_SLEEP_010101", matrixcolumnnames)
print(f"y.shape={y.shape}")
#print(y)

# check the range of sleep time
#print(f"Sleep Time min = {np.min(y)}")
#print(f"Sleep Time mean = {np.mean(y)}")
#print(f"Sleep Time max = {np.max(y)}")
#print(f"Sleep Time std = {np.std(y)}")

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

with open('data.pkl', 'wb') as file:
    data_dict = {"training_data": trainingdata, "training_results": trainingresults, "validation_data": validationdata, "validation_results": validationresults}
    pickle.dump(data_dict, file)


#Analysis:

# linear regression algorithm
print("START Linear Regression training")
validation_stats, linear_models = LinearRegression.s_folds_validation(trainingdata, trainingresults, 5)
print(f"LR Mean: {validation_stats['mean']}")
print(f"LR STD: {validation_stats['std']}")
print(f"LR ALL RMSE: {validation_stats['all_rmse']}")

# save the linear regression model
with open('linear_regression.pkl', 'wb') as file:
    linear_dict = {"model": linear_models, "stats": validation_stats}
    pickle.dump(linear_dict, file)


# linear regression gradient algorithm
print("START Linear Regression Gradient training")
validation_stats, linear_models = LinearRegressionGradient.s_folds_validation(trainingdata, trainingresults, 5)
print(f"LR Gradient Mean: {validation_stats['mean']}")
print(f"LR Gradient STD: {validation_stats['std']}")

# save the linear regression gradient model
with open('linear_regression_gradient.pkl', 'wb') as file:
    gradient_dict = {"model": linear_models, "stats": validation_stats}
    pickle.dump(gradient_dict, file)


# knn regression algorithm
# gets statistics for all k_values but only the last k_value is used for ensemble
print("START k Nearest Neighbors training")
k_values = [int(np.sqrt(trainingdata.shape[0]))]
for k in k_values:
    knn = KNN.KNN(trainingdata, trainingresults, k=k)
    knn_predictions = knn.predict(validationdata)

    # save the KNN model
    with open('knn.pkl', 'wb') as file:
        pickle.dump(knn_predictions, file)

    # statistics
    knn_mse = Statistics.ComputeMSE(validationresults, knn_predictions)
    knn_rmse = Statistics.ComputeRMSE(validationresults, knn_predictions)
    knn_mae = Statistics.ComputeMAE(validationresults, knn_predictions)
    knn_r2 = Statistics.ComputeR2(validationresults, knn_predictions)
    print(f"KNN k={k} MSE: {knn_mse}")
    print(f"KNN k={k} RMSE: {knn_rmse}")
    print(f"KNN k={k} MAE: {knn_mae}")
    print(f"KNN k={k} R2: {knn_r2}")
