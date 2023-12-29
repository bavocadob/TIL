import sys

input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))

dp = [[0] * N for _ in range(N)]

for i in range(N):
    dp[i][i] = 1

for i in range(N - 1):
    if numbers[i] == numbers[i + 1]:
        dp[i][i + 1] = 1

for i in range(2, N):
    for j in range(N - i):
        if numbers[i + j] == numbers[j] and dp[j + 1][i + j - 1] == 1:
            dp[j][i + j] = 1

for _ in range(int(input())):
    s, e = map(lambda x: int(x) - 1, input().split())
    print(dp[s][e])
