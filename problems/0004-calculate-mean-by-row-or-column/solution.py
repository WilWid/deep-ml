def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    
    means = []

    if mode == 'column':

        for j in range(len(matrix[0])): # 10
            tmp = 0
            for i in range(len(matrix)): # 3
                tmp += matrix[i][j]
            means.append(tmp/len(matrix))

    else:
        
        for i in range(len(matrix)): # 3
            tmp = 0
            for j in range(len(matrix[0])): # 10
                tmp += matrix[i][j]
            means.append(tmp/len(matrix[0]))
    

    return means