import sys
from collections import deque

input = sys.stdin.readline

INF = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())

A = [list(input()) for _ in range(N)]

princess_queue = deque()
soldier_queue = deque()
end_x, end_y = -1, -1

princess_visited = [[INF] * M for _ in range(N)]
soldier_visited = [[INF] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if A[i][j] == '@':
            princess_queue.append((i, j))
            A[i][j] = '.'
            princess_visited[i][j] = 0
        elif A[i][j] == '$':
            soldier_queue.append((i, j))
            A[i][j] = '.'
            soldier_visited[i][j] = 0
        elif A[i][j] == '%':
            end_x, end_y = i, j

while princess_queue:
    x, y = princess_queue.popleft()
    if A[x][y] == '%':
        break
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and princess_visited[nx][ny] == INF and A[nx][ny] != '#':
            princess_visited[nx][ny] = princess_visited[x][y] + 1
            princess_queue.append((nx, ny))

while soldier_queue:
    x, y = soldier_queue.popleft()
    if A[x][y] == '%':
        break
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and soldier_visited[nx][ny] == INF and A[nx][ny] != '#':
            soldier_visited[nx][ny] = soldier_visited[x][y] + 1
            soldier_queue.append((nx, ny))

if princess_visited[end_x][end_y] >= soldier_visited[end_x][end_y]:
    print('No')
else:
    print('Yes')
