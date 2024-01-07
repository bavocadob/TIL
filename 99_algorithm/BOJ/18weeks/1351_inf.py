from collections import defaultdict


def solve(x):
    if dp[x] != 0:
        return dp[x]

    dp[x] = solve(x // p) + solve(x // q)

    return dp[x]


n, p, q = map(int, input().split())

dp = defaultdict(int)
dp[0] = 1

print(solve(n))