N, K = map(int, input().split())

mod = 1_000_000_000

dp = [[0] * (N + 1) for _ in range(K + 1)]
dp[0][0] = 1


for i in range(1, K + 1):
    for j in range(N + 1):
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % mod

print(dp)
print(dp[K][N])
