import sys

input = sys.stdin.readline

N, K = map(int, input().split())

dp = [999999] * (K + 1)

dp[0] = 0

coins = [int(input()) for _ in range(N)]

for coin in coins:
    for i in range(coin, K + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[K] != 999999:
    print(dp[K])
else:
    print(-1)

