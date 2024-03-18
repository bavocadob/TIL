import sys

sys.setrecursionlimit(10 ** 6)

n, k = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]


def solve(a, b):
    if dp[a][b] != -1:
        return dp[a][b]
    dp[a][b] = 1

    for i in range(a + 1, n):
        if arr[a] > arr[i] and b > 0:
            dp[a][b] = max(dp[a][b], solve(i, b - 1) + 1)
        if arr[a] <= arr[i]:
            dp[a][b] = max(dp[a][b], solve(i, b) + 1)

    return dp[a][b]


print(solve(0, k))
