import sys

sys.setrecursionlimit(100000)

divide = 1_000_000_000


def solution(depth, index):
    if dp[depth][index] is not None:
        return dp[depth][index]

    if index == 0:
        dp[depth][index] = solution(depth - 1, index + 1)
    elif index == 9:
        dp[depth][index] = solution(depth - 1, index - 1)
    else:
        dp[depth][index] = (solution(depth - 1, index - 1) + solution(depth - 1, index + 1)) % divide

    return dp[depth][index]


N = int(input())

dp = [[None] * 10 for _ in range(N + 1)]

dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(10):
    solution(N, i)
print(sum(dp[N]) % divide)
