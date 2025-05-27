def matrix_multiply(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    if cols1 != rows2:
        raise ValueError("Matrices cannot be multiplied due to incompatible dimensions.")

    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]
result_matrix = matrix_multiply(matrix_a, matrix_b)