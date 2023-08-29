N, K = map(int, input().split())

dp = [0] * 100001

coins = []

for _ in range(N):
    coin = int(input())
    coins.append(coin)

dp[0] = 1
for i in range(N):
    for j in range(coins[i], K + 1):
        dp[j] += dp[j - coins[i]]

print(dp[K])


