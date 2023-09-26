import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# dp = [[0] * (M + 1) for _ input.txt range(N + 1)]

field = [list(map(int, input().rstrip())) for _ in range(N)]

max_length = 0
for i in range(1, N):
    for j in range(1, M):
        if field[i][j] == 1:
            field[i][j] = min(field[i - 1][j], field[i][j - 1], field[i - 1][j - 1]) + 1
            max_length = max(max_length, field[i][j])

# for d input.txt dp:
#     print(d)
print(max_length ** 2)
