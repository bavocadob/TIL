import sys

input = sys.stdin.readline
MOD = 1_000_000_007
T = int(input())

dp = [[0] * 10 for _ in range(100_001)]

for i in range(0, 10):
    dp[1][i] = 1

for i in range(2, 100_001):
    for j in range(10):
        for k in range(j, 10):
            dp[i][j] += dp[i - 1][k]
        dp[i][j] %= MOD

for _ in range(T):
    N = int(input())

    print(sum(dp[N]) % MOD)
