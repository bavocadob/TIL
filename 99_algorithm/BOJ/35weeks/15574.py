import sys

input = sys.stdin.readline
N = int(input())

A = [tuple(map(int, input().split())) for _ in range(N)]
A.sort()

dp = [0.0] * N

for i in range(1, N):
    x1, y1 = A[i]

    for j in range(i):
        x2, y2 = A[j]

        if x1 == x2:
            break

        dist = (abs(y2 - y1) ** 2 + abs(x2 - x1) ** 2) ** 0.5
        dp[i] = max(dp[i], dp[j] + dist)

print(max(dp))
