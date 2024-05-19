import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

INF = int(1e9)
N, M = map(int, input().split())

field = [[0] * M for _ in range(N)]
queue = deque()

building_cnt = 0

for i in range(N):
    temp = input().rstrip()
    for j in range(M):
        if temp[j] == '*':
            field[i][j] = 1
            building_cnt += 1
        elif temp[j] == '#':
            field[i][j] = 2
            building_cnt += 1
        elif temp[j] == '|':
            field[i][j] = INF
        elif temp[j] == '@':
            queue.append((i, j, 2))

cnt = 0

while queue:
    x, y, damage = queue.popleft()
    for k in range(4):
        for kk in range(1, damage + 1):
            nx, ny = x + dx[k] * kk, y + dy[k] * kk
            if not (0 <= nx < N and 0 <= ny < M):
                continue

            if field[nx][ny] == INF:
                break

            next_damage = 0
            if field[nx][ny] > 0:
                field[nx][ny] -= 1

                if field[nx][ny] == 0:
                    next_damage = 1
                    cnt += 1
            queue.append((nx, ny, next_damage))

print(cnt, building_cnt - cnt)
