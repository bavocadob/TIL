import sys

input = sys.stdin.readline

MOD = 1000000007

ans = [0] * 501
dp = [[0] * 501 for _ in range(5001)]

for i in range(10):
    dp[i][1] = 1
ans[1] = 10

for k in range(2, 501):
    R = k * 10
    for j in range(10):
        for i in range(j, R):
            dp[i][k] += dp[i - j][k - 1]
            dp[i][k] %= MOD

    for i in range(R):
        ans[k] += dp[i][k] * dp[i][k]
        ans[k] %= MOD

T = int(input())
for t in range(1, T + 1):
    x = int(input())
    print(f"Case #{t}: {ans[x]}")
