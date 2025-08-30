import numpy as np
from typing import Any

def ComputeAccuracy(actual: np.ndarray, predicted: np.ndarray) -> float:
    comparisonmatrix: np.ndarray = actual == predicted
    sum: float = np.sum(comparisonmatrix)
    accuracy: float = sum / actual.shape[0]
    return accuracy

def GenerateConfusionMatrix(yValidation: np.ndarray, yPredicted: np.ndarray) -> tuple[np.ndarray, list[float]]:
    actualdistinctvalues: np.ndarray = np.unique(yValidation)
    predicteddistinctvalues: np.ndarray = np.unique(yPredicted)
    fromboth: np.ndarray = np.concatenate((actualdistinctvalues, predicteddistinctvalues), axis=0)
    distinctvalues: list[float] = np.unique(fromboth).tolist()

    confusionmatrix: np.ndarray = np.zeros((len(distinctvalues), len(distinctvalues)))
    for i in range(len(yValidation)):
        predicted: float = yPredicted[i]
        actual: float = yValidation[i]
        predictedIndex: int = distinctvalues.index(predicted)
        actualIndex: int = distinctvalues.index(actual)
        confusionmatrix[predictedIndex, actualIndex] = confusionmatrix[predictedIndex, actualIndex] + 1

    return (confusionmatrix, distinctvalues)

def PrintConfusionMatrix(c: np.ndarray, values: list[Any]):
    for predictedIndex in range(len(values)):
        for actualIndex in range(len(values)):
            observationcount: int = c[predictedIndex, actualIndex]
            if observationcount > 0:
                predictedvalue: Any = values[predictedIndex]
                actualvalue: Any = values[actualIndex]
                result: str = "Correct" if predictedvalue == actualvalue else "Incorrect"

                resultstring: str = f"Predicted: {predictedvalue}, Actual: {actualvalue}: {observationcount} observations ({result})"
                print(resultstring)



def ComputeMSE(actual: np.ndarray, predicted: np.ndarray):
    # mean squared error
    return float(np.mean((actual - predicted) ** 2))

def ComputeRMSE(actual: np.ndarray, predicted: np.ndarray):
    # root mean squared error
    return np.sqrt(np.mean((actual - predicted) ** 2))

def ComputeMAE(actual: np.ndarray, predicted: np.ndarray):
    # mean absolute error
    return np.mean(np.abs(actual - predicted))

def ComputeR2(actual: np.ndarray, predicted: np.ndarray):
    # r-squared coefficient of determination
    ss_residual = np.sum((actual - predicted) ** 2)
    ss_total = np.sum((actual - np.mean(actual)) ** 2)
    return 1 - (ss_residual / ss_total)
