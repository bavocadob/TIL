import sys
from collections import deque

input = sys.stdin.readline

# 8방
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def bfs(x, y):
    flag = True

    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if farm[nx][ny] == farm[x][y] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                elif farm[nx][ny] > farm[x][y]:
                    flag = False

    return flag


N, M = map(int, input().split())

farm = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]

ans = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            visited[i][j] = True
            ans += bfs(i, j)

print(ans)
