import sys

input = sys.stdin.readline
sys.setrecursionlimit(100_000)


def dp(depth, index):
    if result[depth][index] is not None:
        return result[depth][index]

    curr_value = triangle[depth][index]

    if index == 0:
        result[depth][index] = dp(depth - 1, index) + curr_value
    elif index == depth:
        result[depth][index] = dp(depth - 1, index - 1) + curr_value
    else:
        result[depth][index] = max(dp(depth - 1, index - 1) + curr_value,
                                   dp(depth - 1, index) + curr_value)

    return result[depth][index]


N = int(input())

triangle = [list(map(int, input().split())) for _ in range(N)]

result = [[None] * i for i in range(1, N + 1)]
result[0][0] = triangle[0][0]

for i in range(N):
    dp(N - 1, i)

print(max(result[N - 1]))
