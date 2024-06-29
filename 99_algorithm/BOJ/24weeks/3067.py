import sys

input = sys.stdin.readline

for _ in range(int(input())):

    N = int(input())

    coins = list(map(int, input().split()))
    T = int(input())

    dp = [0] * (T + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, T + 1):
            if dp[i - coin] != 0:
                dp[i] += dp[i - coin]

    print(dp[T])
