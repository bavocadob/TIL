import sys

input = sys.stdin.readline

while True:

    N, M = map(int, input().split())
    if (N, M) == (0, 0):
        break

    candies = [list(map(int, input().split())) for _ in range(N)]

    col_dp = [[[0] * M for _ in range(N)] for _ in range(2)]

    for i in range(N):
        for j in range(M):
            for k in range(2):
                if j == 0:  # 제일 왼쪽 사탕에 대해서
                    if k == 1:  # 주웠을 때

                        col_dp[k][i][j] = candies[i][j]
                        # 안주우면 어차피 0이라서 패스
                    continue

                if k == 0:  # 안주울때
                    col_dp[k][i][j] = max(col_dp[0][i][j - 1], col_dp[1][i][j - 1])  # 안주울땐 왼쪽거 줍거나 안주운거 중에 더 많은거
                else:  # 주울때
                    col_dp[k][i][j] = col_dp[0][i][j - 1] + candies[i][j]  # 주울땐 옆에거 못줍고 자기거 더해야함

    row_dp = [[0] * N for _ in range(2)]  # 행에 대한 dp

    row_dp[1][0] = max(max(col_dp[0][0]), max(col_dp[1][0]))

    for i in range(1, N):
        for k in range(2):
            if k == 0:  # 해당 행을 안사용할 때
                row_dp[k][i] = max(row_dp[0][i - 1], row_dp[1][i - 1])
            else:  # 해당 행에서 사탕을 주울때
                row_dp[k][i] = row_dp[0][i - 1] + max(max(col_dp[0][i]), max(col_dp[1][i]))

    result = max(row_dp[0][N - 1], row_dp[1][N - 1])

    print(result)
