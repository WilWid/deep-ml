def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    import numpy as np

    trace = matrix[0][0] + matrix[1][1]
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    discriminant = (trace / 2) ** 2 - det

    lambda_1 = trace / 2 + np.sqrt(discriminant)
    lambda_2 = trace / 2 - np.sqrt(discriminant)

    eigenvalues = [lambda_1, lambda_2]

    return eigenvalues