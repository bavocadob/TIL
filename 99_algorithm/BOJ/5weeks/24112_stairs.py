import sys

MOD = 1234567
input = sys.stdin.readline

N, K = map(int, input().split())

stairs = [int(input()) for _ in range(N)]

valid_idx = [0] * (N + 1)
l = 0
distance = 0

for r in range(N + 1):
    while r > l and distance > K:
        # print(l, r, distance)
        distance -= stairs[l]
        l += 1

    valid_idx[r] = l

    if r < N:
        distance += stairs[r]

# print(valid_idx)

dp = [0] * (N + 1)
sum_dp = [0] * (N + 2)

dp[0] = 1
sum_dp[1] = 1

for i in range(1, N + 1):
    dp[i] = (sum_dp[i] - sum_dp[valid_idx[i]]) % MOD
    sum_dp[i + 1] = (sum_dp[i] + dp[i]) % MOD

print(dp[N])



# dp = [0] * (N + 1)
# dp[0] = 1
#
# for i in range(1, N + 1):
#     distance = stairs[i]
#     for j in range(i - 1, -1, -1):
#         dp[i] = (dp[i] + dp[j]) % 1234567
#         distance += stairs[j]
#         if distance > K:
#             break

# print(dp[N])
