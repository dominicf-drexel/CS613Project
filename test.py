import pickle
import LinearRegression
import LinearRegressionGradient
import KNN
import numpy as np
import Statistics

with open('linear_regression.pkl', "rb") as file:
    linear_dict = pickle.load(file)
    linear_models = linear_dict["model"]
    linear_stats = linear_dict["stats"]

with open('linear_regression_gradient.pkl', "rb") as file:
    gradient_dict = pickle.load(file)
    gradient_models = gradient_dict["model"]
    gradient_stats = gradient_dict["stats"]

with open('knn.pkl', "rb") as file:
    knn_predictions = pickle.load(file)

with open('data.pkl', "rb") as file:
    data_dict = pickle.load(file)
    trainingdata = data_dict["training_data"]
    trainingresults = data_dict["training_results"]
    validationdata = data_dict["validation_data"]
    validationresults = data_dict["validation_results"]


# predictions from all linear regression models
# S-fold * runs = number of models
# So if S-fold=5 then 5*100 models
print("START Run the linear regression model")
print("20 runs and 5 folds each * 2 = 200 models")
all_lr_predictions = []
for run_models in linear_models: # 20 runs (hardcoded in LinearRegression.py)
    for model in run_models: # 5 (hardcoded in this file)
        lr_pred = model.predict(validationdata)
        all_lr_predictions.append(lr_pred)

print("START Run the linear regression gradient model")
all_gd_predictions = []
for run_models in gradient_models: # 20 runs (hardcoded in LinearRegression.py)
    for model in run_models: # 5 (hardcoded in this file)
        lr_gd = LinearRegressionGradient.LinearRegressionGradient()
        lr_gd.fit(trainingdata, trainingresults)
        lr_gd_pred = lr_gd.predict(validationdata)
        all_gd_predictions.append(lr_gd_pred)

# average ALL linear regression predictions and KNN
print("START Run the ensemble algorithm, which includes the KNN algorithm")
ensemble_predictions = []
for i in range(len(validationdata)):
    lr_aggregate_prediction = np.mean([pred[i] for pred in all_lr_predictions])
    gd_aggregate_prediction = np.mean([pred[i] for pred in all_gd_predictions])
    final_ensemble_prediction = (lr_aggregate_prediction + gd_aggregate_prediction + knn_predictions[i]) / 3
    ensemble_predictions.append(final_ensemble_prediction)

ensemble_predictions = np.array(ensemble_predictions)

print(f"ensemble_predictions = {ensemble_predictions}")
ensemble_mse = Statistics.ComputeMSE(validationresults, ensemble_predictions)
ensemble_rmse = Statistics.ComputeRMSE(validationresults, ensemble_predictions)
print(f"Ensemble MSE: {ensemble_mse}")
print(f"Ensemble RMSE: {ensemble_rmse}")
    
