import sys

input = sys.stdin.readline

INF = float('inf')


while True:
    S = input().split()
    if S[0] == '0' and S[1] == '0.00':
        break

    N, M = int(S[0]), int(float(S[1]) * 100 + 0.5)

    candies = []
    for _ in range(N):
        candy = input().split()
        cal, cost = int(candy[0]), int(float(candy[1]) * 100 + 0.5)
        candies.append((cal, cost))

    dp = [-INF] * (M + 1)
    dp[0] = 0

    for i in range(N):
        cal, cost = candies[i]
        for j in range(cost, M + 1):
            if dp[j - cost] != -INF:
                dp[j] = max(dp[j], dp[j - cost] + cal)

    print(max(dp))
