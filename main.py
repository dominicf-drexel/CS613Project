import numpy as np
from DataLoad import LoadATUSExtract
from CreateFeatures import TransformIntoFeatures
from MatrixCreation import RowsToMatrix, ExtractX, ExtractY
from DataOperations import GenerateTrainingValidationIndices, GenerateTrainingValidationIndicesByFeatureValue, GetSubset
import KNN

#
#Load data:
filepath: str = "./data/atus_00003.csv"
(rowsdata, columnnames) = LoadATUSExtract(filepath)
#print(columnnames)

(readyrows, readycolumns) = TransformIntoFeatures(rowsdata, columnnames)
print(readycolumns)

(matrixdata, matrixcolumnnames) = RowsToMatrix(readyrows, readycolumns)
print(matrixcolumnnames)

#Create Training, Validation data:
x: np.ndarray
xcolumnnames: list[str]
x, xcolumnnames = ExtractX(matrixdata, matrixcolumnnames, True)
print(x.shape)

y: np.ndarray = ExtractY(matrixdata, "ACT_WORK", matrixcolumnnames)
print(y.shape)
#print(y)

# (trainingindices, validationindices) = GenerateTrainingValidationIndices(x, 0)
(trainingindices, validationindices) = GenerateTrainingValidationIndicesByFeatureValue(x, 0, matrixcolumnnames, "YEAR")
(trainingdata, trainingresults) = GetSubset(x, y, trainingindices)
(validationdata, validationresults) = GetSubset(x, y, validationindices)

#
#Analysis:
# TODO add linear regression algorithm
linear_predictions = []

# knn regression algorithm
# returns predictions as np.array
#knn = KNN(x_train, y_train, k=5)
#predictions = knn.predict(x_test)
knn_predictions = []

# TODO ensemble algorithm
ensemble_predictions = []
for i in range(len(x_test)):
    predictions = []

    # add the linear regression predictions
    for pred in linear_predictions:
        predictions.append(pred[i])

    # add the knn regression predictions
    predictions.append(knn_predictions[i])
    
    # ensemble algorithm
    
    

