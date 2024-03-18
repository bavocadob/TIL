INF = int(1e9)
A, B, C, K = map(int, input().split())

# A 좌로돌아 B 우로돌아 C 뒤로 돌아

dp = [INF] * (K + 1)

form = [(A + B, 2), (A + A + C, 3), (B + B + C, 3), (C + C, 2), (A * 4, 4), (B * 4, 4)]

dp[0] = 0

for i in range(1, K + 1):
    for energy, cost in form:
        if i < energy or dp[i - energy] == INF:
            continue

        dp[i] = min(dp[i], dp[i - energy] + cost)

if dp[K] == INF:
    print(-1)
else:
    print(dp[K])
