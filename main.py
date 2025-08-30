import numpy as np
from DataLoad import LoadATUSExtract
from CreateFeatures import TransformIntoFeatures
from MatrixCreation import RowsToMatrix, ExtractX, ExtractY
import KNN

# comment for test commit - need to delete this

filepath: str = "./data/atus_00003.csv"
(rowsdata, columnnames) = LoadATUSExtract(filepath)
#print(columnnames)

(readyrows, readycolumns) = TransformIntoFeatures(rowsdata, columnnames)
#print(readycolumns)

(matrixdata, matrixcolumnnames) = RowsToMatrix(readyrows, readycolumns)
print(matrixcolumnnames)

x: np.ndarray = ExtractX(matrixdata, matrixcolumnnames, True)
print(x.shape)

y: np.ndarray = ExtractY(matrixdata, "ACT_WORK", matrixcolumnnames)
print(y.shape)
#print(y)


# TODO split data
#x_train = x.copy()
#y_train = y.copy()
x_test = x.copy()

# TODO add linear regression algorithm
linear_preditions = []

# knn regression algorithm
# returns predictions as np.array
#knn = KNN(x_train, y_train, k=5)
#predictions = knn.predict(x_test)
knn_predictions = []

# TODO ensemble algorithm
ensemble_predictions = []
for i in range(len(x_test)):
    preditions = []

    # add the linear regression predictions
    for pred in linear_preditions:
        predictions.append(pred[i])

    # add the knn regression predictions
    predictions.append(knn_predictions[i]
    
    # ensemble algorithm
    
    

