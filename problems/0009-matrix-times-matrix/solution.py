def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    
    mA = len(a[0])
    nB = len(b)
    c = []

    if mA == nB:
        for i in range(len(a)):
            tmp = []
            for j in range(len(b[0])):
                tmpscal = 0
                for k in range(mA):
                    tmpscal += a[i][k] * b[k][j]
                tmp.append(tmpscal)
            c.append(tmp)
    else:
        return -1

    return c