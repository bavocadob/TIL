import sys

import math


input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())

sea = [list(map(int, input().split())) for _ in range(N)]

iceberg = set()

for i in range(N):
    for j in range(M):
        if sea[i][j] > 0:
            iceberg.add((i, j))

day = 1
while iceberg:
    melted = set()

    for x, y in iceberg:
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in iceberg:
                sea[x][y] -= 1

        if sea[x][y] <= 0:
            sea[x][y] = 0
            melted.add((x, y))

    iceberg = iceberg.difference(melted)

    stack = []

    visited = [[True] * M for _ in range(N)]
    for ice in iceberg:
        x, y = ice
        visited[x][y] = False
        if not stack:
            visited[x][y] = True
            stack.append((x, y))

    while stack:
        x, y = stack.pop()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                stack.append((nx, ny))
                visited[nx][ny] = True

    end = False
    for ice in iceberg:
        x, y = ice
        if not visited[x][y]:
            end = True
            break

    if end:
        print(day)
        break
    day += 1
else:
    print(0)
