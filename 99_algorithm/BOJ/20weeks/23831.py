import sys

input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())

dp = [[[[-1] * 2 for _ in range(N + 1)] for _ in range(A + 1)] for _ in range(N + 1)]

dp[0][0][0][0] = 0

# dp[a][b][c][d] = a일에 요양을 b번만큼하고 소학습실을 c번만큼 채운거중에 d일 연속으로 휴게실을 쓴 경우
for i in range(1, N + 1):
    p, q, r, s = map(int, input().split())
    p = max(p, q)

    # 정독실 or 소학습실 쓰는 경우
    for j in range(A + 1):
        # j는 요양일 수
        for k in range(1, N + 1):
            # k는 학습실 채운 회수
            for t in range(2):
                # p는 연속으로 휴게실 쓴 회수
                if dp[i - 1][j][k - 1][t] != -1:
                    dp[i][j][k][0] = max(dp[i - 1][j][k - 1][t] + p, dp[i][j][k][0])

    # 요양 하는 경우
    for j in range(1, A + 1):
        # j는 요양일 수
        for k in range(N + 1):
            # k는 소학습실 채운 회수
            for t in range(2):
                # p는 연속으로 휴게실 쓴 회수
                if dp[i - 1][j - 1][k][t] != -1:
                    dp[i][j][k][0] = max(dp[i - 1][j - 1][k][t] + s, dp[i][j][k][0])

    # 휴게실 사용하는 경우
    for j in range(A + 1):
        # j는 요양일 수
        for k in range(N + 1):
            # k는 소학습실 채운 회수
            if dp[i - 1][j][k][0] != -1:
                dp[i][j][k][1] = max(dp[i - 1][j][k][0] + r, dp[i][j][k][1])

ans = 0
for i in range(A + 1):
    for j in range(B, N + 1):
        for k in range(2):
            ans = max(ans, dp[N][i][j][k])

print(ans)
