import sys

input = sys.stdin.readline

N = int(input())

weights = [int(input()) for _ in range(N)]

dp = [(0, 0)] * (N + 1)

for i in range(N - 1, -1, -1):
    dp[i] = max(dp[i + 1], (dp[i + 1][1] + weights[i], dp[i + 1][0]))

print(*dp[0])
