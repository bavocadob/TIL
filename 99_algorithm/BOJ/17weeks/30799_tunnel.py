MOD = 998_244_353

S = int(input())

dp = [[0] * 8 for _ in range(S + 1)]
dp[0][0] = 1

for i in range(1, S + 1):
    for j in range(8):
        if j:
            if j < 7:
                dp[i][j] = (dp[i - 1][j] * 6 + dp[i - 1][j - 1]) % MOD
            else:
                dp[i][j] = (dp[i - 1][j] * 7 + dp[i - 1][j - 1]) % MOD
        else:
            dp[i][j] = (dp[i - 1][j] * 6) % MOD

print(dp[S][7])
