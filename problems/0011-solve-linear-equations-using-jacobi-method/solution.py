import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    import numpy as np

    dim = len(A)
    xold = np.zeros(dim)
    xnew = np.zeros(dim)

    for k in range(n):
        for i in range(dim):
            tmp = 0
            for j in range(dim):
                if i != j:
                    tmp += A[i][j] * xold[j]
            xnew[i] = (1 / A[i][i]) * (b[i] - tmp)
        xold = xnew.copy()


    return xnew