import sys
input = sys.stdin.readline

N = int(input())

heights = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (N + 1) for _ in range(N + 1)]


for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            continue

        row_cost = 999999
        col_cost = 999999
        if i != 0:
            if heights[i][j] < heights[i - 1][j]:
                row_cost = 0
            else:
                row_cost = heights[i][j] - heights[i - 1][j] + 1

        if j != 0:
            if heights[i][j] < heights[i][j - 1]:
                col_cost = 0
            else:
                col_cost = heights[i][j] - heights[i][j - 1] + 1

        dp[i + 1][j + 1] = min(dp[i][j + 1] + row_cost, dp[i + 1][j] + col_cost)

print(dp[N][N])



