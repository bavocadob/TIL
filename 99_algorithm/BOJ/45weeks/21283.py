import sys

SCORE = [0, 10, 19, 27, 34, 40, 45, 49, 52, 54, 55]


def max_score(d, r1, r2):
    if d == N + 2:
        return 0
    if dp[d][r1][r2] != -1:
        return dp[d][r1][r2]

    res = 0
    max_eat = min(10, r1 + r2 + fruits[d])

    for eat in range(min(10, r2), max_eat + 1):
        e2 = min(eat, r2)
        e1 = min(eat - e2, r1)
        e0 = min(eat - e1 - e2, fruits[d])

        score = SCORE[eat] + max_score(
            d + 1,
            fruits[d] - e0,
            r1 - e1,
        )
        res = max(res, score)

    dp[d][r1][r2] = res
    return res


N = int(sys.stdin.readline().strip())
fruits = list(map(int, sys.stdin.readline().split())) + [0, 0]

dp = [[[-1] * 31 for _ in range(31)] for _ in range(N + 2)]

print(max_score(0, 0, 0))
