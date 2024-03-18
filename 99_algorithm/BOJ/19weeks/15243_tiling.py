def solve(N):
    if N % 2 == 1:
        return 0

    dp = [0] * (N + 1)
    dp[0] = 1
    dp[2] = 3

    for i in range(4, N + 1, 2):
        dp[i] = (dp[i - 2] * 3) % MOD

        for j in range(4, i + 1, 2):
            dp[i] += dp[i - j] * 2
            dp[i] %= MOD

    return dp[N]


MOD = 1_000_000_007
N = int(input())
print(solve(N))
