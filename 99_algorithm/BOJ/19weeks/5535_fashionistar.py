import sys

input = sys.stdin.readline

N, M = map(int, input().split())

weather = [int(input()) for _ in range(N)]

dp = [[0] * M for _ in range(N)]

clothes = []

for i in range(M):
    a, b, c = map(int, input().split())
    clothes.append((a, b, c))

    if weather[0] < a or weather[0] > b:
        dp[0][i] = -1

for i in range(1, N):
    for j in range(M):
        if weather[i] > clothes[j][1] or weather[i] < clothes[j][0]:
            dp[i][j] = -1
            continue

        for k in range(M):
            if dp[i - 1][k] == -1:
                continue

            dp[i][j] = max(dp[i][j], dp[i - 1][k] + (abs(clothes[k][2] - clothes[j][2])))

ans = -1

for i in range(M):
    ans = max(ans, dp[N - 1][i])

print(ans)
