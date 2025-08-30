import random
from typing import Tuple
import numpy as np

def generateTrainingValidationLists(indexlist: list[int], seed: int) -> Tuple[list[int], list[int]]:
    random.seed(seed)
    random.shuffle(indexlist)

    training: list[int] = []
    validation: list[int] = []

    cutoff: float =  2.0 * (len(indexlist) / 3.0)
    for i in range(len(indexlist)):
        index: int = indexlist[i]
        if (i < cutoff):
            training.append(index)
        else:
            validation.append(index)

    return (training, validation)

def GenerateTrainingValidationIndices(x: np.ndarray, seed: int) -> Tuple[list[int], list[int]]:
    rowrnd: list[int] = list(range(x.shape[0]))
    return generateTrainingValidationLists(rowrnd, seed)

def GetSubset(x: np.ndarray, y: np.ndarray, indices: list[int]) -> Tuple[np.ndarray, np.ndarray]:
    subsetlistx: list[np.ndarray] = []
    subsetlisty: list[np.ndarray] = []
    
    for i in range(len(indices)):
        index: int = indices[i]
        subsetlistx.append(x[index, :])
        subsetlisty.append(y[index])
        
    subsetx: np.ndarray = np.array(subsetlistx)
    subsety: np.ndarray = np.array(subsetlisty)
    return (subsetx, subsety)

def FindSubsetXIndicesForFeatureValue(x: np.ndarray, featureindex: int, featurevalue: object) -> list[int]:
    subsetindices: list = []

    for i in range(x.shape[0]):
        rowfeaturevalue: object = x[i, featureindex]
        if (rowfeaturevalue == featurevalue):
            subsetindices.append(i)

    return subsetindices

def GenerateTrainingValidationIndicesByFeatureValue(x: np.ndarray, seed: int, columnnames: list[str], featurecolumn: str) -> Tuple[list[int], list[int]]:
    featureindex: int = columnnames.index(featurecolumn)
    featurevalues: list = np.unique(x[:, featureindex]).tolist()

    training: list[int] = []
    validation: list[int] = []

    for featurevalue in featurevalues:
        indices: list[int] = FindSubsetXIndicesForFeatureValue(x, featureindex, featurevalue)
        (training_thisvalue, validation_thisvalue) = generateTrainingValidationLists(indices, seed)
        training.extend(training_thisvalue)
        validation.extend(validation_thisvalue)

    return (training, validation)
