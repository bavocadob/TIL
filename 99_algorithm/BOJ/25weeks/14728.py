N, T = map(int, input().split())

items = []

for _ in range(N):
    cost, value = map(int, input().split())
    items.append((cost, value))

dp = [-1] * (T + 1)
dp[0] = 0

for cost, value in items:
    for i in range(T, cost - 1, -1):
        if dp[i - cost] != -1:
            dp[i] = max(dp[i - cost] + value, dp[i])

print(max(dp))
