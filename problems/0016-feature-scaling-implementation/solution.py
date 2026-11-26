import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    standardized_data = np.zeros(np.shape(data))
    normalized_data = np.zeros(np.shape(data))
    #print(np.shape(data))

    for i in range(len(data[0])):
        tmp = data[:,i]
        
        normalized_data[:,i] = ((tmp - np.min(tmp)) / (np.max(tmp) - np.min(tmp)))

        standardized_data[:,i] = (tmp - np.mean(tmp)) / np.std(tmp)
    

    return standardized_data.tolist(), normalized_data.tolist()