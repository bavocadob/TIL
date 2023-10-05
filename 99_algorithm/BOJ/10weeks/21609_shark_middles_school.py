import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def pull_arr(arr, x, y):
    for i in range(x - 1, -1, -1):
        if arr[i][y] == -1:
            return
        elif arr[i][y] is not None:
            arr[x][y] = arr[i][y]
            arr[i][y] = None
            return


def gravity(arr):
    for j in range(N):
        for i in range(N - 1, 0, -1):
            if arr[i][j] is None:
                pull_arr(arr, i, j)


def rotate(arr):
    rotated_arr = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            rotated_arr[i][j] = arr[j][N - 1 - i]

    for i in range(N):
        for j in range(N):
            arr[i][j] = rotated_arr[i][j]


def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N


def bfs(x, y):
    queue = deque([(x, y)])
    block_set = {(x, y)}
    block_num = play[x][y]
    rainbow_cnt = 0
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if not is_valid(nx, ny) or visited[nx][ny]:
                continue

            if play[nx][ny] == 0 or play[nx][ny] == block_num:
                block_set.add((nx, ny))
                visited[nx][ny] = True
                queue.append((nx, ny))
                if play[nx][ny] == 0:
                    rainbow_cnt += 1

    return block_set, rainbow_cnt


N, M = map(int, input().split())

play = [list(map(int, input().split())) for _ in range(N)]

ans = 0

while True:
    visited = [[False] * N for _ in range(N)]
    rainbow_block = []

    for i in range(N):
        for j in range(N):
            if play[i][j] == 0:
                rainbow_block.append((i, j))

    max_set = set()
    max_r_cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and play[i][j] is not None and play[i][j] != 0 and play[i][j] != -1:
                b_set, r_cnt = bfs(i, j)
                if len(b_set) > len(max_set):
                    max_set = b_set
                    max_r_cnt = r_cnt
                elif len(b_set) == len(max_set):
                    if r_cnt >= max_r_cnt:
                        max_set = b_set
                        max_r_cnt = r_cnt

                for rx, ry in rainbow_block:
                    visited[rx][ry] = False

    if len(max_set) < 2:
        break

    ans += len(max_set) ** 2
    for block_x, block_y in max_set:
        play[block_x][block_y] = None

    # for p in play:
    #     print(p)
    # print('-------------논처리')

    gravity(play)
    # for p in play:
    #     print(p)
    # print('-------------1차중력')
    rotate(play)
    # for p in play:
    #     print(p)
    # print('-------------회전')
    gravity(play)
    # for p in play:
    #     print(p)
    # print('-------------2차중력')

print(ans)
