import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def solve():
    queue = deque()
    queue.append((sx, sy))
    visited = [[-1] * M for _ in range(N)]

    visited[sx][sy] = 0

    while queue:
        x, y = queue.popleft()
        if x == 0 or x == N - 1 or y == 0 or y == M - 1:
            return visited[x][y]

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if not (0 <= nx < N and 0 <= ny < M) or wall[nx][ny] == '1' or visited[nx][ny] != -1:
                continue

            if wall[nx][ny] in keys:
                px, py = keys[wall[nx][ny]]
                if nx + px != x or ny + py != y:
                    continue

            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))

    return -1


keys = {'U': (-1, 0), 'R': (0, 1), 'L': (0, -1), 'D': (1, 0)}

T, N, M = map(int, input().split())

wall = [input().rstrip() for _ in range(N)]

sx, sy = -1, -1

for i in range(N):
    if sx != -1:
        break
    for j in range(M):
        if wall[i][j] == 'S':
            sx, sy = i, j
            break

rst = solve()

if rst != -1 and rst <= T:
    print(rst)
else:
    print('NOT POSSIBLE')
