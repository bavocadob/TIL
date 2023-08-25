import sys

sys.stdin = open('input.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N and not visited[x][y]


def dfs(x, y, height, step, removable):
    global max_cnt

    if step > max_cnt:
        max_cnt = step

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if is_valid(nx, ny):
            if mountain[nx][ny] < height:
                visited[nx][ny] = True
                dfs(nx, ny, mountain[nx][ny], step + 1, removable)
                visited[nx][ny] = False
            else:
                if removable:
                    if height > mountain[nx][ny] - K:
                        visited[nx][ny] = True
                        dfs(nx, ny, height - 1, step + 1, False)
                        visited[nx][ny] = False


T = int(input())

for tc in range(T):
    N, K = map(int, input().split())

    mountain = [list(map(int, input().split())) for _ in range(N)]

    start_list = []
    max_height = 0
    for i in range(N):
        for j in range(N):
            if max_height < mountain[i][j]:
                max_height = mountain[i][j]
                start_list.clear()

            if max_height == mountain[i][j]:
                start_list.append((i, j))

    max_cnt = 0

    visited = [[False] * N for _ in range(N)]

    for i, j in start_list:
        visited[i][j] = True
        dfs(i, j, mountain[i][j], 1, True)
        visited[i][j] = False

    print(f'#{tc + 1} {max_cnt}')
