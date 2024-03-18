def get_score(number):
    score = 0
    while number:
        score += number % 2
        number //= 2
    return score


N = int(input())

cards = list(map(int, input().split()))

if N == 1:
    print(get_score(0))
elif N == 2:
    print(get_score(cards[0] ^ cards[1]))
else:
    dp = [-1] * N

    dp[1] = get_score(cards[0] ^ cards[1])
    dp[2] = get_score(cards[0] ^ cards[1] ^ cards[2])

    for i in range(3, N):
        if dp[i - 2] != -1:
            dp[i] = max(dp[i], dp[i - 2] + get_score(cards[i] ^ cards[i - 1]))

        if dp[i - 3] != -1:
            dp[i] = max(dp[i - 3] + get_score(cards[i] ^ cards[i - 1] ^ cards[i - 2]), dp[i])

    print(max(dp[N - 1], 0))
