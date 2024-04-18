import sys

input = sys.stdin.readline


def solve(left, right, pos):
    # pos 0은 left의 위치에 1은 right의 위치에 존재
    if left == 0 and right == N - 1:
        return 0

    if dp[left][right][pos] != INF:
        return dp[left][right][pos]

    curr = loc[right] if pos == 1 else loc[left]
    w = pre[N] - (pre[right + 1] - pre[left])

    if left > 0:
        dp[left][right][pos] = min(dp[left][right][pos],
                                   solve(left - 1, right, 0) + w * (curr - loc[left - 1]))

    if right < N - 1:
        dp[left][right][pos] = min(dp[left][right][pos],
                                   solve(left, right + 1, 1) + w * (loc[right + 1] - curr))

    return dp[left][right][pos]


INF = int(1e9)
N, M = map(int, input().split())

loc = []
cost = []
pre = [0] * (N + 1)

for i in range(N):
    a, b = map(int, input().split())
    loc.append(a)
    cost.append(b)
    pre[i + 1] = pre[i] + b

dp = [[[INF] * 2 for _ in range(N)] for _ in range(N)]

print(solve(M - 1, M - 1, 0))
