import sys

input = sys.stdin.readline

INF = int(1e9)

N = int(input())

A = [0] + list(map(int, input().split()))

dp = [[[-INF] * 512 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    dp[i][i][A[i]] = 1

for i in range(1, N):
    for j in range(i + 1, N + 1):
        for k in range(512):
            a = dp[i + 1][j][k]
            b = dp[i][j - 1][k]
            c = dp[i + 1][j][k ^ A[i]] + 1
            d = dp[i][j - 1][k ^ A[j]] + 1
            dp[i][j][k] = max(a, b, c, d, dp[i][j][k])

Q = int(input())

for _ in range(Q):
    l, r = map(int, input().split())
    ans = 0
    for k in range(512):
        ans = max(ans, dp[l][r][k] + k)
    print(ans)
