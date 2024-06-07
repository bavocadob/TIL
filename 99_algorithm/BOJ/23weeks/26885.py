import sys
from collections import deque

input = sys.stdin.readline


def bfs(queue: deque, visited: list):
    while queue:
        x, y = queue.popleft()

        if visited[x][y]:
            continue

        visited[x][y] = True
        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]

            if not (0 <= nx < N and 0 <= ny < M) or visited[nx][ny] or field[nx][ny] == '#':
                continue

            queue.append((nx, ny))


def check(a, b):
    for i in range(N):
        for j in range(M):
            if a[i][j] and b[i][j]:
                return True

    return False


dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, 2, -2, 2, -2, 1, -1]

N, M = map(int, input().split())

field = [list(input()) for _ in range(N)]

visited_a = [[False] * M for _ in range(N)]
visited_b = [[False] * M for _ in range(N)]

queue_a = deque()
queue_b = deque()

for i in range(N):
    for j in range(M):
        if field[i][j] == 'H':
            field[i][j] = '.'
            if queue_a:
                queue_b.append((i, j))
                break
            else:
                queue_a.append((i, j))

bfs(queue_a, visited_a)
bfs(queue_b, visited_b)

rst = check(visited_a, visited_b)

if rst:
    print('JA')
else:
    print('NEJ')
