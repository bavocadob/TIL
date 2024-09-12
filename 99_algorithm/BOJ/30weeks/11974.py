import sys

input = sys.stdin.readline
N = int(input())

prefix_sum = [0]

for i in range(N):
    prefix_sum.append(prefix_sum[-1] + int(input()))

dp = [list() for _ in range(8)]

for i in range(N + 1):
    dp[prefix_sum[i] % 7].append(i)

ans = 0

for i in range(8):
    if len(dp[i]) >= 2:
        ans = max(ans, dp[i][-1] - dp[i][0])

print(ans)