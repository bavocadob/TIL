import sys

input = sys.stdin.readline

MOD = 1_000_000_007


def bell_number(N):
    dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(1, N + 1):
        for j in range(1, i + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] * j
            dp[i][j] %= MOD

    rst = []

    for i in range(N + 1):
        rst.append(sum(dp[i]) % MOD)
    return rst


def find(x):
    if parents[x] == x:
        return x

    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    px, py = find(x), find(y)
    if px == py:
        return False

    if px > py:
        px, py = py, px

    parents[py] = px
    return True


MAX = 5000
N, M = map(int, input().split())

size = N

parents = [i for i in range(N + 1)]
ans = bell_number(N)

for _ in range(M):
    a, b = map(int, input().split())

    if union(a, b):
        size -= 1

    print(ans[size])
