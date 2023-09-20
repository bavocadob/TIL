import heapq
import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())

cornfield = [list(map(int, input().split())) for _ in range(N)]

queue = []
visited = [[False] * M for _ in range(N)]
for i in range(N):
    visited[i][0] = True
    heapq.heappush(queue, (-cornfield[i][0], i, 0))

    if M > 1:
        visited[i][M - 1] = True
        heapq.heappush(queue, (-cornfield[i][M - 1], i, M - 1))

for j in range(1, M - 1):
    visited[0][j] = True
    heapq.heappush(queue, (-cornfield[0][j], 0, j))
    if N > 1:
        visited[N - 1][j] = True
        heapq.heappush(queue, (-cornfield[N - 1][j], N - 1, j))

K = int(input())

for _ in range(K):
    value, x, y = heapq.heappop(queue)
    print(x + 1, y + 1)
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            heapq.heappush(queue, (-cornfield[nx][ny], nx, ny))
