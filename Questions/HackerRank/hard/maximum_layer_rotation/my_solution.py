def encryptMatrix(matrix, n, m):
    newMatrix = []
    count = 0
    mini = min(n, m)
    while count <= mini - 1:
        dum = []
        i = count
        for k1 in range(i, m - count):
            dum.append(matrix[i][k1])

        for k2 in range(i + 1, n - count):
            dum.append(matrix[k2][k1])
        if mini - 1 != count:
            for k1 in range(k1 - 1, count - 1, -1):
                dum.append(matrix[k2][k1])
            for k2 in range(k2 - 1, count, -1):
                dum.append(matrix[k2][k1])
        newMatrix.append(dum)
        count += 1
        mini -= 1
    return newMatrix


def decryptMatrix(rotated_list, n, m):
    rotatedMatrix = [[0 for j in range(m)] for i in range(n)]

    mini = min(m, n)
    count = 0

    while count <= mini - 1:
        count1 = 0
        lst = rotated_list[count]
        i = count
        for k1 in range(i, m - count):
            rotatedMatrix[i][k1] = lst[count1]
            count1 += 1

        for k2 in range(i + 1, n - count):
            rotatedMatrix[k2][k1] = lst[count1]
            count1 += 1

        if mini - 1 != count:
            for k1 in range(k1 - 1, count - 1, -1):
                rotatedMatrix[k2][k1] = lst[count1]
                count1 += 1
            for k2 in range(k2 - 1, count, -1):
                rotatedMatrix[k2][k1] = lst[count1]
                count1 += 1

        count += 1
        mini -= 1
    return rotatedMatrix


def matrixRotation(matrix, r):
    n = len(matrix)
    m = len(matrix[0])

    iniList = encryptMatrix(matrix, n, m)

    rotated_list = []
    for lst in iniList:
        len_lst = len(lst)
        r_lst = r % len_lst
        rotated_list.append(lst[r_lst: len_lst] + lst[0: r_lst])

    rotatedMatrix = decryptMatrix(rotated_list, n, m)

    for i in range(n):
        for j in range(m):
            print(rotatedMatrix[i][j], end=" ")
        print()

    return rotatedMatrix
