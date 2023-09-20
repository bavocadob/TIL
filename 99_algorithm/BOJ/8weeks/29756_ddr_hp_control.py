N, K = map(int, input().split())

score = list(map(int, input().split()))
cost = list(map(int, input().split()))

# 체력이 100, 구간이 N개

dp = [[-1] * 101 for _ in range(N + 1)]
dp[0][100] = 0

for i in range(N):
    s, c = score[i], cost[i]

    for j in range(101):
        recovery = min(j + K, 100)
        dp[i + 1][recovery] = max(dp[i][j], dp[i + 1][recovery])

    for j in range(101 - c):
        if dp[i][j + c] != -1:
            next_hp = min(100, j + K)
            dp[i + 1][next_hp] = max(dp[i + 1][next_hp], dp[i][j + c] + s)

print(max(dp[N]))
