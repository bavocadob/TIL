import sys

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N = int(input())

    cards = list(map(int, input().split()))
    dp = [0, -int(1e9)]

    for i in range(1, N + 1):
        card = cards[i - 1]
        temp = [-int(1e9), -int(1e9)]
        if i % 2:
            # 순서 변경 없음
            temp[0] = max(dp[0] + card, temp[0])
            temp[1] = max(dp[1], temp[1])

            # 순서 변경 있음
            temp[0] = max(dp[1], temp[0])
            temp[1] = max(dp[0] + card, temp[1])
        else:
            temp[0] = max(dp[0], temp[0])
            temp[1] = max(dp[1] + card, temp[1])

            temp[0] = max(dp[1] + card, temp[0])
            temp[1] = max(dp[0], temp[1])

        dp[0] = max(temp[0], dp[0])
        dp[1] = max(temp[1], dp[1])

    print(max(dp))
