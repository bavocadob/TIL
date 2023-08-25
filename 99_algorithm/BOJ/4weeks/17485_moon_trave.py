N, M = map(int, input().split())

cost = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0] * M for _ in range(N)] for _ in range(3)]

for i in range(3):
    dp[i][0] = cost[0]

# 0은 왼 -> 오  1은 가운데 2는 오 -> 왼
inf = 99999999
for i in range(1, N):
    dp[0][i][0] = inf
    dp[2][i][M - 1] = inf

for i in range(1, N):
    for j in range(M):
        if j > 0:
            dp[0][i][j] = min(dp[1][i - 1][j - 1], dp[2][i - 1][j - 1]) + cost[i][j]
        dp[1][i][j] = min(dp[0][i - 1][j], dp[2][i - 1][j]) + cost[i][j]
        if j < M - 1:
            dp[2][i][j] = min(dp[0][i - 1][j + 1], dp[1][i - 1][j + 1]) + cost[i][j]

min_cost = inf
for i in range(3):
    min_cost = min(min_cost, min(dp[i][N - 1]))

print(min_cost)
