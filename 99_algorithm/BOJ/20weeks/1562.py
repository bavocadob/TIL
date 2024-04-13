MOD = 1_000_000_000

N = int(input())
dp = [[[0] * (1 << 10) for _ in range(N + 1)] for _ in range(10)]

for i in range(1, 10):
    dp[i][1][1 << i] = 1

for i in range(1, N):
    for j in range(10):
        for k in range(1 << 10):
            if j:
                bit = k | 1 << (j - 1)
                dp[j - 1][i + 1][bit] += dp[j][i][k]
                dp[j - 1][i + 1][bit] %= MOD

            if j < 9:
                bit = k | 1 << (j + 1)

                dp[j + 1][i + 1][bit] += dp[j][i][k]
                dp[j + 1][i + 1][bit] %= MOD

print(sum(dp[i][N][(1 << 10) - 1] for i in range(10)) % MOD)
