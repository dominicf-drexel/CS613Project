import numpy as np
from DataLoad import LoadATUSExtract
from CreateFeatures import TransformIntoFeatures
from MatrixCreation import RowsToMatrix, ExtractX, ExtractY

# comment for test commit - need to delete this

filepath: str = "../data/atus_00003.csv"
(rowsdata, columnnames) = LoadATUSExtract(filepath)
print(columnnames)

(readyrows, readycolumns) = TransformIntoFeatures(rowsdata, columnnames)
print(readycolumns)

(matrixdata, matrixcolumnnames) = RowsToMatrix(readyrows, readycolumns)
print(matrixcolumnnames)

x: np.ndarray = ExtractX(matrixdata, matrixcolumnnames, True)
print(x.shape)

y: np.ndarray = ExtractY(matrixdata, "ACT_WORK", matrixcolumnnames)
print(y.shape)
print(y)
