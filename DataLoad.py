import csv
from typing import Tuple

def LoadATUSExtract(filepath: str, ) -> Tuple[list, list]:
    columnnames: list[str] = []
    
    rowsdata: list = []
    with open(filepath, mode='r') as file:
        reader = csv.reader(file)

        #column names in first data row:
        columnnames = next(reader)

        for row in reader:
            rowdata: list = []
            
            rowsdata.append(row)

    return (rowsdata, columnnames)
