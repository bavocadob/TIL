import sys

from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def valid(x, y):
    return 0 <= x < N and 0 <= y < M


def need_jump(x1, y1, x2, y2):
    return maze[x1][y1] < maze[x2][y2]


def bfs():
    queue = deque([(start_x - 1, start_y - 1, F)])

    while queue:
        x, y, hp = queue.popleft()

        if (x, y) == (end_x - 1, end_y - 1):
            print('잘했어!!')
            return

        if hp == 0:
            continue

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if valid(nx, ny) and (not visited[nx][ny] or visited[nx][ny] < hp - 1):
                jump = need_jump(x, y, nx, ny)
                if not jump or (hp >= maze[nx][ny] - maze[x][y]):
                    visited[nx][ny] = hp - 1
                    queue.append((nx, ny, hp - 1))

    print('인성 문제있어??')


T = int(input())

for _ in range(T):

    N, M, O, F, start_x, start_y, end_x, end_y = map(int, input().split())

    maze = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    visited[start_x - 1][start_y - 1] = F

    for _ in range(O):
        i, j, h = map(int, input().split())
        maze[i - 1][j - 1] = h

    bfs()
