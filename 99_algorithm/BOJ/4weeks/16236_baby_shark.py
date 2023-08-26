import sys
input = sys.stdin.readline

from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

N = int(input())

queue = deque()
field = []

shark_find = False
for i in range(N):
    space = list(map(int, input().split()))

    if not shark_find:
        for j in range(N):
            if space[j] == 9:
                space[j] = 0
                queue.append((i, j, 0))
                shark_find = True
    field.append(space)

time = 0
eat = 0
level = 2
visited = [[False] * N for _ in range(N)]

while queue:
    eatable_lst = []

    while queue:
        x, y, distance = queue.popleft()

        if eatable_lst:
            if distance > eatable_lst[-1][2]:
                break
        if 0 < field[x][y] < level:
            eatable_lst.append((x, y, distance))

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if level >= field[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, distance + 1))

    if eatable_lst:
        eatable_lst.sort(key=lambda fish: [-fish[2], -fish[0], -fish[1]])
        # print(eatable_lst)
        x, y, distance = eatable_lst[-1]
        field[x][y] = 0
        visited = [[False] * N for _ in range(N)]
        time += distance
        eat += 1
        if eat == level:
            level += 1
            eat = 0

        queue = deque([(x, y, 0)])
    else:
        break

print(time)
