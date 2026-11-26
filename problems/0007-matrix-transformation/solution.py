import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
    import numpy as np

    detT = np.linalg.det(T)
    detS = np.linalg.det(S)
    T = np.array(T)
    S = np.array(S)

    if detT != 0 and detS != 0:
        return np.linalg.solve(T,A @ S)
    else:
        return -1


    return transformed_matrix