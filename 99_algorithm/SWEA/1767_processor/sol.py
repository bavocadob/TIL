# 코드가 더러워서 수정해야함

import sys

sys.stdin = open('input.txt')


def dfs(depth, line_cnt, install_cnt):
    global max_core, min_line

    if install_cnt > max_core:
        max_core = install_cnt
        min_line = line_cnt
    elif install_cnt == max_core:
        min_line = min(min_line, line_cnt)

    if depth == len(core_idx):
        return

    x, y = core_idx[depth]
    for k in range(4):
        if line_candidate[(x, y)][k]:
            can_install = True
            nx, ny = x + dx[k], y + dy[k]
            while 0 <= nx < N and 0 <= ny < N:
                if circuit[nx][ny] == 1:
                    can_install = False
                    break
                nx, ny = nx + dx[k], ny + dy[k]

            if can_install:
                nx, ny = x + dx[k], y + dy[k]
                while 0 <= nx < N and 0 <= ny < N:
                    circuit[nx][ny] = 1
                    line_cnt += 1
                    nx, ny = nx + dx[k], ny + dy[k]
                dfs(depth + 1, line_cnt, install_cnt + 1)

                nx, ny = x + dx[k], y + dy[k]
                while 0 <= nx < N and 0 <= ny < N:
                    circuit[nx][ny] = 0
                    line_cnt -= 1
                    nx, ny = nx + dx[k], ny + dy[k]

    dfs(depth + 1, line_cnt, install_cnt)


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())

for tc in range(T):

    max_core = 0
    min_line = 999999

    N = int(input())

    circuit = [list(map(int, input().split())) for _ in range(N)]

    line_candidate = dict()
    core_idx = []

    for i in range(N):
        for j in range(N):
            if circuit[i][j] == 1:  # 1이면 후보군 등록시작
                line_candidate[(i, j)] = [False] * 4
                core_idx.append((i, j))
                if i == 0:
                    line_candidate[(i, j)][0] = True
                    continue
                elif i == N - 1:
                    line_candidate[(i, j)][1] = True
                    continue
                elif j == 0:
                    line_candidate[(i, j)][2] = True
                    continue
                elif j == N - 1:
                    line_candidate[(i, j)][3] = True
                    continue

                for k in range(4):
                    nx, ny = i, j
                    while nx != 0 and ny != 0 and nx != N - 1 and ny != N - 1:
                        nx, ny = nx + dx[k], ny + dy[k]
                        if circuit[nx][ny] == 1:
                            break
                    else:
                        line_candidate[(i, j)][k] = True

    dfs(0, 0, 0)
    print(f'#{tc+1} {min_line}')
