import sys

input = sys.stdin.readline

N = int(input())

temp = list(map(int, input().split()))
min_dp = temp[:]
max_dp = temp[:]

for i in range(N - 1):
    temp = list(map(int, input().split()))
    temp_max_dp = max_dp[:]
    temp_min_dp = min_dp[:]
    temp_max_dp[0] = max(max_dp[0], max_dp[1]) + temp[0]
    temp_max_dp[1] = max(max_dp[0], max_dp[1], max_dp[2]) + temp[1]
    temp_max_dp[2] = max(max_dp[1], max_dp[2]) + temp[2]
    temp_min_dp[0] = min(min_dp[0], min_dp[1]) + temp[0]
    temp_min_dp[1] = min(min_dp[0], min_dp[1], min_dp[2]) + temp[1]
    temp_min_dp[2] = min(min_dp[1], min_dp[2]) + temp[2]

    max_dp = temp_max_dp
    min_dp = temp_min_dp

# print(max_dp, min_dp)
print(max(max_dp), min(min_dp))

