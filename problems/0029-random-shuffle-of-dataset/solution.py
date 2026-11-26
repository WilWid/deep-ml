import numpy as np

def shuffle_data(X, y, seed=None):
    
    np.random.seed(seed)
    permute = np.random.permutation(X.shape[0])
    
    X = X[permute,:]
    y = y[permute]

    return (X,y)