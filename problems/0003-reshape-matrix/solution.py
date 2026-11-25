import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    #Write your code here and return a python list after reshaping by using numpy's tolist() method
    a = np.array(a)
    a_shape = np.shape(a)
    if a_shape[0] * a_shape[1] != new_shape[0] * new_shape[1]:
        return []
    else:
        result = []
        a = a.flatten()
        count = 0
        for _ in range(new_shape[0]):
            tmp = []
            for _ in range(new_shape[1]):
                tmp.append(a[count])
                if count < len(a):
                    count += 1
            result.append(tmp)
        return result
    #return reshaped_matrix