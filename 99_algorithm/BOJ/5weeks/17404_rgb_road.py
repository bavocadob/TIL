import sys

input = sys.stdin.readline

N = int(input())

costs = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0] * 3 for _ in range(N)] for _ in range(3)]

for i in range(3):
    dp[i][0][i] = costs[0][i]
    dp[i][0][(i + 1) % 3], dp[i][0][(i + 2) % 3] = 999999, 999999

for k in range(3):
    for i in range(1, N):
        for j in range(3):
            dp[k][i][j] = min(dp[k][i - 1][(j + 1) % 3], dp[k][i - 1][(j + 2) % 3]) + costs[i][j]

result = 999999

for i in range(3):
    result = min(result, dp[i][N - 1][(i + 1) % 3], dp[i][N - 1][(i + 2) % 3])

print(result)
