N = int(input())
A = list(map(int, input().split()))

dp = [[0, 0] for _ in range(N + 1)]
result = 0

for i in range(1, N + 1):
    temp = A[i - 1]
    j = (temp - 1) % 2

    dp[i][temp % 2] = dp[i - 1][temp % 2] + 1

    if dp[i - 1][j] > 0:
        dp[i][j] = dp[i - 1][j] - 1

    result = max(result, dp[i][temp % 2])

print(result)
