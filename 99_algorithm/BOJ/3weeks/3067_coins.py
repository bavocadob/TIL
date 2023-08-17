for tc in range(int(input())):
    N = int(input())

    coins = list(map(int, input().split()))

    M = int(input())

    dp = [0] + [10000000] * M

    for coin in coins:
        for i in range(coin, M + 1):
            if dp[i - coin] != 10000000:
                dp[i] = min(dp[i], dp[i-coin] + 1)

    print(dp)
