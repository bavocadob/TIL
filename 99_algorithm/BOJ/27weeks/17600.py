def solve():
    for i in range(1, 100001):
        min_value = float('inf')
        for c in A:
            if c <= i:
                min_value = min(min_value, dp[i - c] + 1)
        dp.append(min_value if min_value != float('inf') else 0)

        max_value = -float('inf')
        for c in A:
            if c <= i:
                max_value = max(max_value, c)
        g.append(g[i - max_value] + 1)

        if dp[i] != g[i]:
            print(i)
            return

    print(-1)


N = int(input())

A = list(map(int, input().split()))

dp = [0]
g = [0]

solve()
