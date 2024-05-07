INF = int(1e9)
n, m = map(int, input().split())

dp = [[INF] * 2 for _ in range(m + 1)]

dp[n][0] = 0

for i in range(n + 1, m + 1):
    if dp[i - 1][0] != INF:
        dp[i][0] = min(dp[i][0], dp[i - 1][0] + 1)

    if dp[i - 1][1] != INF:
        dp[i][1] = min(dp[i][1], dp[i - 1][1] + 1)

    if i % 2 == 0:
        if dp[i // 2][0] != INF:
            dp[i][0] = min(dp[i][0], dp[i // 2][0] + 1)

        if dp[i // 2][1] != INF:
            dp[i][1] = min(dp[i][1], dp[i // 2][1] + 1)

    if i % 10 == 0:
        if dp[i // 10][0] != INF:
            dp[i][1] = min(dp[i][1], dp[i // 10][0] + 1)

print(min(dp[m][0], dp[m][1]))

