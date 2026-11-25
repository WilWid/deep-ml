def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    m = len(a[0])
    n = len(b)
    result = []

    if n != m:
        return -1
    else:
        for i in range(len(a)):
            tmp = 0
            for j in range(len(a[0])):
                tmp += a[i][j] * b[j]
            result.append(tmp)
        return result
    pass