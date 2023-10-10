from collections import deque
import sys

input = sys.stdin.readline


def valid(x_, y_):
    return 0 <= x_ < N and 0 <= y_ < M


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N, M = map(int, input().split())

queue = deque()

maze = [list(input()) for _ in range(N)]

fires = []

visited = [[0] * M for _ in range(N)]
j_x = 0
j_y = 0
for i in range(N):
    for j in range(M):
        if maze[i][j] == 'J':
            visited[i][j] = 1
            j_x = i
            j_y = j
            maze[i][j] = '.'
        elif maze[i][j] == 'F':
            queue.append((0, i, j))

queue.append((1, j_x, j_y))

while queue:
    t, x, y = queue.popleft()

    if t and (not x or not y or x == N - 1 or y == M - 1):
        print(visited[x][y])
        break

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if not valid(nx, ny) or maze[nx][ny] != '.':
            continue

        if t:
            if visited[nx][ny]:
                continue
            visited[nx][ny] = visited[x][y] + 1
        else:
            maze[nx][ny] = 'F'

        queue.append((t, nx, ny))
else:
    print('IMPOSSIBLE')
