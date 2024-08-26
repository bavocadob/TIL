import sys

input = sys.stdin.readline
N, K, M = map(int, input().split())

dp = [0] * 500_001

for _ in range(M):
    temp = input()

A = list(map(int, input().split()))

for i in range(N * K):
    x = A[i]
    dp[x] += 1
    print(dp[x], end=" ")
