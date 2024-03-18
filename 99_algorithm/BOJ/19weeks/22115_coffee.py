N, M = map(int, input().split())

INF = 1000
coffee = list(map(int, input().split()))

dp = [INF] * (M + 1)
dp[0] = 0

for c in coffee:
    for i in range(M, c - 1, -1):
        if dp[i - c] != INF:
            dp[i] = min(dp[i - c] + 1, dp[i])

if dp[M] == INF:
    print(-1)
else:
    print(dp[M])
