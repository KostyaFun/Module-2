def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix
result1 = get_matrix(2,2,10)
print(result1)
result2 = get_matrix(3, 5, 15)
print(result2)
result3 = get_matrix(4,1, 7)
print(result3)
