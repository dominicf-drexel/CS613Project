from typing import Tuple
import numpy as np

def RowsToMatrix(readyrows: list[list[str]], readycolumnnames: list[str]) -> Tuple[np.ndarray, list[str]]:
    returnmatrix: np.ndarray = np.array(readyrows)
    return (returnmatrix, readycolumnnames)

def ExtractX(rowmatrix: np.ndarray, columnnames: list[str], removedataqualityflags: bool) -> Tuple[np.ndarray, list[str]]:
    IDENTIFIERFIELDS: list[str] = ["CASEID","SERIAL","PERNUM","LINENO"]

    xcolumnnames: list[str] = []

    toremoveindices: list[int] = []
    for i in range(len(columnnames)):
        columnname: str = columnnames[i]

        if columnname in IDENTIFIERFIELDS:
            toremoveindices.append(i)
            continue
        
        if columnname.startswith("ACT_"):
            toremoveindices.append(i)
            continue
        
        if (removedataqualityflags):
            if columnname.startswith("Q"):
                toremoveindices.append(i)
                continue

        xcolumnnames.append(columnname)

    x: np.ndarray = np.delete(rowmatrix, toremoveindices, axis=1)
    return (x, xcolumnnames)

def ExtractY(rowmatrix: np.ndarray, ycolumnname: str, columnnames: list[str]) -> np.ndarray:
    columnindex: int = columnnames.index(ycolumnname)
    y: np.ndarray = rowmatrix[:, columnindex]
    return y
