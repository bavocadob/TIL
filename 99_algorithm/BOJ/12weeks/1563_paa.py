import sys

sys.setrecursionlimit(int(1e9))


def dfs(d, l, a):
    if l == 2 or a == 3:
        return 0

    if dp[d][l][a] != -1:
        return dp[d][l][a]

    if d == N:
        return 1

    dp[d][l][a] = dfs(d + 1, l, 0) + dfs(d + 1, l + 1, 0) + dfs(d + 1, l, a + 1)
    return dp[d][l][a]


MOD = 1_000_000
N = int(input())

dp = [[[-1] * 3 for _ in range(2)] for _ in range(N + 1)]
print(dfs(0, 0, 0) % MOD)
