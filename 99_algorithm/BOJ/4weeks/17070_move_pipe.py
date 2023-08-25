N = int(input())

# 0은 가로, 1은 세로 2는 오른쪽 아래 대각선
# 가로 -> 가로, 대각선
# 세로 -> 세로, 대각선
# 대각선 -> 가로, 세로, 대각선
dp = [[[0] * N for _ in range(N)] for _ in range(3)]
dp[0][0][1] = 1

house = [list(map(int, input().split())) for _ in range(N)]


for i in range(N):
    for j in range(1, N):
        if i == 0 and j == 1:
            continue
        if house[i][j] == 0:
            dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1]
            if i < 1:
                continue
            dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]
            if house[i - 1][j] == 1 or house[i][j - 1] == 1:
                continue

            dp[2][i][j] = dp[0][i - 1][j - 1] + dp[1][i - 1][j - 1] + dp[2][i - 1][j - 1]

result = 0
for i in range(3):
    # print(dp[i])
    result += dp[i][N- 1][N - 1]

print(result)
