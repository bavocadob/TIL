import sys

from collections import deque

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def solution(x, y):
    queue = deque([(x, y)])
    visited = [[0] * M for _ in range(N)]
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and treasure_map[nx][ny] == 'L' and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

    return visited[x][y] - 1


N, M = map(int, input().split())

treasure_map = [list(input().rstrip()) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(M):
        if treasure_map[i][j] == 'L':
            ans = max(ans, solution(i, j))

print(ans)
