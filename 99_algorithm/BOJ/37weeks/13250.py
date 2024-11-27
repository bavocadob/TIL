N = int(input())

dp = [0] * (N + 1)
dp[0] = 0
dp[1] = 1

if N >= 2:
    dp[2] = (dp[0] + dp[1]) / 6 + 1
if N >= 3:
    dp[3] = (dp[0] + dp[1] + dp[2]) / 6 + 1
if N >= 4:
    dp[4] = (dp[0] + dp[1] + dp[2] + dp[3]) / 6 + 1
if N >= 5:
    dp[5] = (dp[0] + dp[1] + dp[2] + dp[3] + dp[4]) / 6 + 1

for i in range(6, N + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4] + dp[i - 5] + dp[i - 6]) / 6 + 1

print(dp[N])
