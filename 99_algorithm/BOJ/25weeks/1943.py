import sys

input = sys.stdin.readline


def solve():
    N = int(input())
    coins = []
    sum_of_coins = 0

    for i in range(N):
        coin, cnt = map(int, input().split())
        sum_of_coins += coin * cnt

        coins.append((coin, cnt))

    if sum_of_coins % 2:
        print(0)
        return

    target = sum_of_coins // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for coin, cnt in coins:
        if dp[target]:
            print(1)
            return

        for value in range(target, coin - 1, -1):
            if dp[value - coin]:
                for i in range(cnt):
                    if value + coin * i <= target:
                        dp[value + coin * i] = True
                    else:
                        break
    if dp[target]:
        print(1)
    else:
        print(0)


for _ in range(3):
    solve()
