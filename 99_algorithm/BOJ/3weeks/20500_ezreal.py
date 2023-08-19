# numbers = [i * 15 for i in range(1, 1000000) if
#            '0' not in str(i * 15) and '0' not in str(i * 15) and '0' not in str(i * 15) and '2' not in str(
#                i * 15) and '3' not in str(i * 15) and '4' not in str(i * 15) and '6' not in str(
#                i * 15) and '7' not in str(i * 15) and '8' not in str(i * 15) and '9' not in str(i * 15)]
# print(numbers)

MOD = 1_000_000_007

N = int(input())

dp = [0] * (N + 2)

dp[1] = dp[2] = 1

for i in range(3, N + 1):
    dp[i] = (dp[i - 2] * 2 + dp[i - 1]) % MOD

print(dp[N - 1])
