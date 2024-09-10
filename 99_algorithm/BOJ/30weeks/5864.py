import sys

input = sys.stdin.readline
N, A, B = map(int, input().split())

num = [0] + [int(input()) for _ in range(N)]
num.sort()

dp = [0.0] * (N + 1)

for i in range(1, N + 1):
    dp[i] = A + (num[i] - num[1]) / 2.0 * B

for i in range(2, N + 1):
    for j in range(1, i):
        dp[i] = min(dp[i], A + (num[i] - num[j + 1]) / 2.0 * B + dp[j])

if dp[N] > int(dp[N]):
    print(f"{int(dp[N])}.5")
else:
    print(int(dp[N]))
