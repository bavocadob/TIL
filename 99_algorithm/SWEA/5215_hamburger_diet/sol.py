import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N, calorie = map(int, input().split())

    dp = [0] + [-1] * calorie

    ingredients = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(calorie, ingredients[i][1] - 1, -1):
            if dp[j - ingredients[i][1]] != -1:
                dp[j] = max(dp[j], dp[j - ingredients[i][1]] + ingredients[i][0])

    print(f'#{tc + 1}{max(dp)}')
