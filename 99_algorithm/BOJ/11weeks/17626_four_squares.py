import math

INF = 4
dp = [0, 1]

N = int(input())

for i in range(2, N + 1):
    v = INF
    for j in range(1, int(math.sqrt(i)) + 1):
        v = min(v, dp[i - j ** 2])
    dp.append(v + 1)

print(dp[N])
