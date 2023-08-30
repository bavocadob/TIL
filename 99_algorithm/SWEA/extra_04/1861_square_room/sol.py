import sys

sys.stdin = open('input.txt')

# from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def valid(x, y):
    return 0 <= x < N and 0 <= y < N


def bfs(x, y):
    global max_distance, min_value
    min_v = max_v = room[x][y]

    queue = [(x, y)]

    while queue:
        x, y = queue.pop()
        min_v = min(min_v, room[x][y])
        max_v = max(max_v, room[x][y])

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if valid(nx, ny) and not visited[room[nx][ny]] and abs(room[nx][ny] - room[x][y]) == 1:
                visited[room[nx][ny]] = True
                queue.append((nx, ny))

    distance = max_v - min_v + 1
    if distance > max_distance:
        max_distance = distance
        min_value = min_v
    elif distance == max_distance:
        min_value = min(min_v, min_value)


T = int(input())

for tc in range(T):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * (N ** 2 + 1)
    max_distance = 0
    min_value = 999999
    for i in range(N):
        for j in range(N):
            if not visited[room[i][j]]:
                visited[room[i][j]] = True
                bfs(i, j)

    print(f'#{tc + 1} {min_value} {max_distance}')