import sys

input = sys.stdin.readline
INF = float('inf')

N, M = map(int, input().split())

dp = [[-INF] * (M + 1) for _ in range(N + 1)]

dp[0][0] = 0

for i in range(1, N + 1):
    dist = int(input())
    dp[i][0] = dp[i - 1][0]

    for j in range(1, M + 1):
        dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + dist)

    for j in range(1, M + 1):
        if j >= i:
            break
        dp[i][0] = max(dp[i][0], dp[i - j][j])

print(dp[N][0])
