def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    cov = []
    for i in range(len(vectors)):
        tmp = []
        for j in range(len(vectors)):
            mysum = 0
            for k in range(len(vectors[0])):
                xibar = sum(vectors[i]) / len(vectors[i])
                xjbar = sum(vectors[j]) / len(vectors[j])
                mysum += (vectors[i][k] - xibar) * (vectors[j][k] - xjbar)
            mysum /= len(vectors[0]) - 1
            tmp.append(mysum)
        cov.append(tmp)


    return cov