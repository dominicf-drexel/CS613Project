import numpy as np
#from DataLoad import LoadATUSExtract
#from CreateFeatures import TransformIntoFeatures
#from MatrixCreation import RowsToMatrix, ExtractX, ExtractY

#filepath: str = "./data/atus_00003.csv"
#(rowsdata, columnnames) = LoadATUSExtract(filepath)

#(readyrows, readycolumns) = TransformIntoFeatures(rowsdata, columnnames)

#(matrixdata, matrixcolumnnames) = RowsToMatrix(readyrows, readycolumns)

#x: np.ndarray = ExtractX(matrixdata, matrixcolumnnames, True)
#bias_column = np.ones((x.shape[0],1))

#BLS_PCARE_SLEEP is not in the dataset given, change "ACT_PCARE" to BLS_PCARE_SLEEP
#y: np.ndarray = ExtractY(matrixdata, "ACT_PCARE", matrixcolumnnames)
#y_reshaped = y.reshape(-1, 1)

#data = np.concatenate((bias_column, x, y_reshaped), axis=1)


class LinearRegression:
    def __init__(self):
        self.weights = None

    def fit(self, x, y):
        bias_column = np.ones((x.shape[0],1))
        data = np.concatenate((bias_column, x), axis=1)
        
        # core linear regression math
        x_t = np.transpose(data)
        n = x_t @ y
        d = np.linalg.pinv(x_t @ data)
        self.weights = d @ n
    
    def predict(self, x):
        # add a bias column to the data before making predictions
        bias_column = np.ones((x.shape[0],1))
        data = np.concatenate((bias_column, x), axis=1)        
        predictions = data @ self.weights
        return predictions



def s_folds_validation(x, y, S):
    bias_column = np.ones((x.shape[0],1))
    processed_data = np.concatenate((bias_column, x, y.reshape(-1,1)), axis=1)   
    
    rmse_array = np.empty(20)
    for i in range(20):
        np.random.seed(i)
        np.random.shuffle(processed_data)

        folds = np.array_split(processed_data, S, axis=0)
        squared_error_array = np.empty(S)

        for fold in range(S):
            validation = folds[fold]
            training = np.concatenate(folds[:fold] + folds[fold+1:], axis=0)

            X_TRAIN = training[:, :-1]
            X_VAL = validation[:, :-1]
            
            Y_TRAIN = training[:,-1]
            Y_VAL = validation[:,-1]

            #X_TRAIN_T = np.transpose(X_TRAIN)
            
            #n = X_TRAIN_T @ Y_TRAIN
            #d = np.linalg.pinv(X_TRAIN_T @ X_TRAIN)
            
            #W_TRAIN = d @ n
            
            #Y_VAL_PREDICTED = X_VAL @ W_TRAIN

            lr = LinearRegression()
            lr.fit(X_TRAIN, Y_TRAIN)
            Y_VAL_PREDICTED = lr.predict(X_VAL)

            
            squared_error = (Y_VAL - Y_VAL_PREDICTED)**2
            mse = np.mean(squared_error)
            squared_error_array = np.append(squared_error_array, mse)

        mse_total = np.mean(squared_error_array)
        rmse = np.sqrt(mse_total)
        rmse_array[i] = rmse

    mean = np.mean(rmse_array)
    std = np.std(rmse_array)

    print(f"{S} Fold Statistics:")
    print("Mean: ", mean)
    print("Standard Deviation: ", std) 

#s_folds_validation(data, 3)
#s_folds_validation(data, 223)
#s_folds_validation(data, 1338)


