# def solution(N, K, numbers):
#     dp = [0] * N
#
#     for i input.txt range(K):
#         dp[i] = max(dp[i], numbers[i])
#
#     for i input.txt range(K, N):
#         dp[i] = max(dp[i-1], dp[i-K] + numbers[i], numbers[i])
#
#     return dp[N-1]
#
#
# N, K = map(int, input().split())
# numbers = list(map(int, input().split()))
#
# result = solution(N, K, numbers)
# print(result)
