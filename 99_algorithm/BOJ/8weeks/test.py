MOD = 1_000_000


def matrix_multiply(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD

    return C


def matrix_power(matrix, n):
    if n == 0:
        size = len(matrix)
        result = [[0] * size for _ in range(size)]
        for i in range(size):
            result[i][i] = 1
        return result
    elif n % 2 == 0:
        half_power = matrix_power(matrix, n // 2)
        return matrix_multiply(half_power, half_power)
    else:
        half_power = matrix_power(matrix, (n - 1) // 2)
        return matrix_multiply(matrix_multiply(half_power, half_power), matrix)


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_matrix = [[1, 1], [1, 0]]

        result_matrix = matrix_power(fib_matrix, n - 1)

        return result_matrix[0][0]


N = int(input())
print(fibonacci(N))
