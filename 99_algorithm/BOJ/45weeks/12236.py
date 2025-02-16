import sys

input = sys.stdin.readline


def solve():
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().split()))

    order = sorted(range(n), key=lambda x: a[x])

    INF = float('inf')
    dp = [[INF] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for k in range(n):
        curr_order = order[k]
        for i in range(k):
            if order[i] < order[k]:
                curr_order -= 1

        for i in range(k + 1):
            j = k - i
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + curr_order)
            dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + (n - k - 1 - curr_order))

    return min(dp[i][n - i] for i in range(n + 1))


T = int(sys.stdin.readline().strip())
for t in range(1, T + 1):
    ans = solve()
    print(f"Case #{t}: {ans}")
