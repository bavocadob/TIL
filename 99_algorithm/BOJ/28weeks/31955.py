r, c, p = map(int, input().split())
dp = [[0.0 for _ in range(c)] for _ in range(r)]

for i in range(r - 1, -1, -1):
    for j in range(c - 1, -1, -1):
        if i == r - 1 and j == c - 1:
            continue

        if i == r - 1:
            dp[i][j] = dp[i][j + 1] + p / 4.0
        elif j == c - 1:
            dp[i][j] = dp[i + 1][j] + p / 4.0
        else:
            diff = min(p, abs(dp[i + 1][j] - dp[i][j + 1]))
            prob = (p + diff) / (2 * p)
            dp[i][j] = prob * min(dp[i + 1][j], dp[i][j + 1])
            dp[i][j] += (prob - 0.5) * diff / 2
            dp[i][j] += (1 - prob) * max(dp[i + 1][j], dp[i][j + 1])

print(dp[0][0])


