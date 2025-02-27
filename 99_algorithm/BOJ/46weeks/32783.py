import math
import sys

input = sys.stdin.readline
MOD = 1_000_000_007
N = int(input())

A = list()

for _ in range(N):
    a, m = map(int, input().split())
    # 소비전력(Wh) :  a * m / 60
    # 비용 = 소비전력(kWh) * 96 = (a * m * 96) / (60 * 1000) = a * m // 625
    cost = (a * m) // 625

    # (250 * a) * (15 * m) = 3750 * (a * m)  // 625 = (a * m) * 6
    A.append(cost // 6)

c1, c2 = map(int, input().split())

c1 = math.ceil(c1 / 6)
c2 //= 6

dp = [0] * (c2 + 1)
dp[0] = 1

for computer in A:
    if computer > c2:
        continue

    for i in range(c2, computer - 1, -1):
        dp[i] = (dp[i] + dp[i - computer]) % MOD

ans = 0

for i in range(c1, c2 + 1):
    ans += dp[i]
    ans %= MOD

print(ans)
