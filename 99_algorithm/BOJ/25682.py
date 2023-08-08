import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

chess_board = [input() for _ in range(n)]

p_sum = [[0] * (m + 1) for _ in range(n + 1)]

color = ['W', 'B']

for i in range(n):
    for j in range(m):
        # i + j =
        # 00 01 02 03 04 05 06 07
        # 10 11 12 13 14 15 16 17

        if chess_board[i][j] == color[(i + j) % 2]:
            p_sum[i + 1][j + 1] += 1

        p_sum[i + 1][j + 1] += p_sum[i + 1][j] + p_sum[i][j + 1] - p_sum[i][j]


min_color = compare_val = k ** 2


for i in range(n - k + 1):
    for j in range(m - k + 1):
        temp_sum = p_sum[i + k][j + k] - p_sum[i][j + k] - p_sum[i + k][j] + p_sum[i][j]
        min_color = min(min_color, temp_sum, compare_val - temp_sum)

print(min_color)