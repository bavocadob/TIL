C, R = map(int, input().split())
MOD = 100000

dp = [[[0 for _ in range(4)] for _ in range(C + 1)] for _ in range(R + 1)]

for i in range(1, R + 1):
    dp[i][1][0] = 1
for j in range(1, C + 1):
    dp[1][j][2] = 1

for i in range(2, R + 1):
    for j in range(2, C + 1):
        dp[i][j][0] = (dp[i - 1][j][1] + dp[i - 1][j][0]) % MOD
        dp[i][j][1] = dp[i - 1][j][2]

        dp[i][j][2] = (dp[i][j - 1][3] + dp[i][j - 1][2]) % MOD
        dp[i][j][3] = dp[i][j - 1][0]

ans = 0
for k in range(4):
    ans += dp[R][C][k]

print(ans % MOD)
