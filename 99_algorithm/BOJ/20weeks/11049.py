import sys

input = sys.stdin.readline


def get_matrix(l1, l2, r2):
    a = A[l1 - 1][0]
    b = A[l2 - 1][1]
    c = A[r2 - 1][1]
    return a * b * c


def solve(left, right):
    if dp[left][right] != INF:
        return dp[left][right]

    for i in range(left, right):
        dp[left][right] = min(dp[left][right],
                              solve(left, i) + solve(i + 1, right) + get_matrix(left, i, right))

    return dp[left][right]


INF = int(1e9)
N = int(input())

A = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(N + 1):
    dp[i][i] = 0

print(solve(1, N))
