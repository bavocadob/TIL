import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * (N + 2)

for i in range(N):
    day, pay = map(int, input().split())
    dp[i + 1] = max(dp[i + 1], dp[i])
    if i + 1 + day <= N + 1:
        dp[i + 1 + day] = max(dp[i + 1 + day], dp[i + 1] + pay)


print(max(dp))
