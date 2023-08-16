import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M, C = map(int, input().split())

cheese_index = []

start = None

cheese_map = []
for i in range(N):
    line = input()
    for j in range(M):
        if line[j].isdigit():
            cheese_index.append((int(line[j]), i, j))
        elif line[j] == 'S':
            start = (i, j, 0)

    cheese_map.append(list(line))

cheese_index.sort()

queue = deque([start])

target_factory = 0

temp_map = deepcopy(cheese_map)

while queue:
    x, y, step = queue.popleft()
    if target_factory == C:
        print(step)
        break
    if (x, y) == (cheese_index[target_factory][1], cheese_index[target_factory][2]):
        target_factory += 1
        queue.clear()
        queue.append((x, y, step))
        temp_map = deepcopy(cheese_map)
        continue

    for k in range(4):

        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and temp_map[nx][ny] != 'X':
            temp_map[nx][ny] = 'X'
            queue.append((nx, ny, step + 1))
