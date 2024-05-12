import sys
from datetime import datetime

input = sys.stdin.readline
date1 = datetime.strptime(input().rstrip(), "%Y %m %d")
date2 = datetime.strptime(input().rstrip(), "%Y %m %d")

diff = date2 - date1

T, N = map(int, input().split())

A = []

for _ in range(N):
    a, b, c = map(int, input().split())

    if a == 1 or a == 2:
        A.append((b, c))
    else:
        A.append((b, c * 30))

dp = [-1] * (T + 1)
dp[0] = 0
for cost, value in A:
    for i in range(T, cost - 1, -1):
        if dp[i - cost] != -1:
            dp[i] = max(dp[i], dp[i - cost] + value)

print(abs(max(dp) - diff.days))
