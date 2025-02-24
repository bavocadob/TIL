import sys

n, k = map(int, sys.stdin.readline().split())
moves = sys.stdin.readline().strip()

start_num = [0] * (2 * n + 2)
start_num[1] = 1

idx = 1
for i in range(2, n + 1):
    start_num[i] = start_num[i - 1] + idx
    idx += 1

for i in range(n + 1, 2 * n):
    start_num[i] = start_num[i - 1] + idx
    idx -= 1

cur_x, cur_y = 0, 0
result = 1

move_map = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}

for move in moves:
    dx, dy = move_map[move]
    cur_x += dx
    cur_y += dy

    pos = cur_x + cur_y
    cur_start = start_num[pos + 1]

    if pos % 2 == 0:
        offset = cur_y if pos < n else abs(n - cur_x - 1)
    else:
        offset = cur_x if pos < n else abs(n - cur_y - 1)

    result += cur_start + offset


print(result)
