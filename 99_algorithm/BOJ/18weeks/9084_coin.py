import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())

    A = list(map(int, input().split()))

    M = int(input())

    dp = [0] * (M + 1)
    dp[0] = 1

    for a in A:
        for i in range(a, M + 1):
            dp[i] += dp[i - a]

    print(dp[M])
