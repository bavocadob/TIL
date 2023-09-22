import sys

from collections import deque

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
N, M = map(int, input().split())

field = [list(input()) for _ in range(N)]

queue = deque()
dochi_x = dochi_y = cave_x = cave_y = None
for i in range(N):
    for j in range(M):
        if field[i][j] == '*':
            queue.append((1, i, j))
        elif field[i][j] == 'S':
            dochi_x, dochi_y = i, j
        elif field[i][j] == 'D':
            cave_x, cave_y = i, j

queue.append((2, dochi_x, dochi_y))
field[dochi_x][dochi_y] = '.'
visited = [[0] * M for _ in range(N)]
# 도치는 2 물은 1
while queue:
    obj, x, y = queue.popleft()

    if field[x][y] == 'D':
        break

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]

        if not (0 <= nx < N and 0 <= ny < M):
            continue

        if obj == 1 and field[nx][ny] == '.':
            field[nx][ny] = '*'
            queue.append((1, nx, ny))
        elif obj == 2 and not visited[nx][ny]:
            if field[nx][ny] == '.' or field[nx][ny] == 'D':
                visited[nx][ny] = visited[x][y] + 1
                queue.append((2, nx, ny))

if visited[cave_x][cave_y]:
    print(visited[cave_x][cave_y])
else:
    print('KAKTUS')
