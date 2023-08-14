# 조금 수정이 필요한 느린 코드

import sys

from collections import deque

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, L, R = map(int, input().split())

country = [list(map(int, input().split())) for _ in range(N)]

stack = []
queue = deque()
unites = []

day = 0

visitied = [[False] * N for _ in range(N)]

while True:
    for i in range(N):
        for j in range(N):
            stack.append((i, j))

    while stack:
        i, j = stack.pop()

        if visitied[i][j]:
            continue

        unite = [(i, j)]
        queue.append((i, j))
        visitied[i][j] = True

        while queue:
            x, y = queue.popleft()

            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < N and 0 <= ny < N and not visitied[nx][ny] and L <= abs(
                        country[x][y] - country[nx][ny]) <= R:
                    visitied[nx][ny] = True
                    unite.append((nx, ny))
                    queue.append((nx, ny))

        if len(unite) > 1:
            unites.append(unite)

    if not unites:
        break

    while unites:
        unite = unites.pop()
        temp_sum = 0
        for x, y in unite:
            temp_sum += country[x][y]

        temp_sum = temp_sum // len(unite)
        for x, y in unite:
            country[x][y] = temp_sum

    day += 1
    visitied = [[False] * N for _ in range(N)]

print(day)
