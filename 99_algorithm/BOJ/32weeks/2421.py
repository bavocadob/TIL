def get_prime():
    limit = 1_000_000
    temp = [True] * (limit + 1)
    temp[0] = temp[1] = False

    for i in range(2, int(limit ** 0.5) + 1):
        if temp[i]:
            for j in range(i * i, limit + 1, i):
                temp[j] = False

    return temp


def concatenate_numbers(i, j):
    num_digits_j = len(str(j))
    return i * (10 ** num_digits_j) + j


is_prime = get_prime()

N = int(input())

dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        concatenate_number = concatenate_numbers(i, j)

        if is_prime[concatenate_number]:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[N][N] - 1)
