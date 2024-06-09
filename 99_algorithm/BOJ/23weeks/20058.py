import sys

from collections import deque
from copy import deepcopy

input = sys.stdin.readline

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def rotate(x, y, length):
    temp = [[0] * length for _ in range(length)]

    for i in range(x, x + length):
        for j in range(y, y + length):
            temp[i - x][j - y] = A[i][j]

    for i in range(x, x + length):
        for j in range(y, y + length):
            A[x + j - y][y + x + length - 1 - i] = temp[i - x][j - y]


def check():
    temp_A = deepcopy(A)

    for i in range(arr_size):
        for j in range(arr_size):
            cnt = 0

            for k in range(4):
                ni, nj = i + dx[k], j + dy[k]

                if 0 <= ni < arr_size and 0 <= nj < arr_size:
                    if temp_A[ni][nj] != 0:
                        cnt += 1

            if cnt < 3:
                A[i][j] = max(0, A[i][j] - 1)


def firestorm(size):
    length = 2 ** size

    for i in range(0, 2 ** N, length):
        for j in range(0, 2 ** N, length):
            rotate(i, j, length)

    check()


def bfs(x, y):
    qqq = deque([(x, y)])
    cnt = 1
    visited[x][y] = True

    while qqq:
        xx, yy = qqq.popleft()

        for k in range(4):
            nx, ny = xx + dx[k], yy + dy[k]

            if 0 <= nx < arr_size and 0 <= ny < arr_size and not visited[nx][ny] and A[nx][ny] > 0:
                cnt += 1
                visited[nx][ny] = True
                qqq.append((nx, ny))

    return cnt


N, Q = map(int, input().split())

arr_size = 2 ** N

A = [list(map(int, input().split())) for _ in range(arr_size)]

queue = list(map(int, input().split()))

for q in queue:
    firestorm(q)

ans = 0
max_cnt = 0

visited = [[False] * arr_size for _ in range(arr_size)]

for i in range(arr_size):
    for j in range(arr_size):
        ans += A[i][j]

        if not visited[i][j] and A[i][j] > 0:
            max_cnt = max(max_cnt, bfs(i, j))

print(ans)
print(max_cnt)
