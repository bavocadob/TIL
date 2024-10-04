def matrix_multiply(mat_a, mat_b, mod):
    return [
        [
            (mat_a[0][0] * mat_b[0][j] + mat_a[0][1] * mat_b[1][j]) % mod for j in range(2)
        ],
        [
            (mat_a[1][0] * mat_b[0][j] + mat_a[1][1] * mat_b[1][j]) % mod for j in range(2)
        ]
    ]


def matrix_power(mat, exp, mod):
    identity_matrix = [[1, 0], [0, 1]]  # 단위 행렬
    while exp > 0:
        if exp % 2 == 1:
            identity_matrix = matrix_multiply(identity_matrix, mat, mod)
        mat = matrix_multiply(mat, mat, mod)
        exp //= 2
    return identity_matrix


def solve(n, mod):
    if n == 0:
        return 2 % mod
    elif n == 1:
        return 4 % mod

    transformation_matrix = [
        [2, 1],
        [0, 1]
    ]

    powered_matrix = matrix_power(transformation_matrix, n - 1, mod)

    fn = (powered_matrix[0][0] * 4 + powered_matrix[0][1] * 1) % mod

    return fn


N, M = map(int, input().split())
print(solve(N, M))
