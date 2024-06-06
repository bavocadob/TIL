import sys

input = sys.stdin.readline
sys.setrecursionlimit(999999)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(x, y, c_idx, d_idx):
    if visited[x][y][c_idx][d_idx]:
        return result[x][y][c_idx][d_idx]

    visited[x][y][c_idx][d_idx] = True

    if field[x][y] == 'E':
        result[x][y][c_idx][d_idx] = True
        return True

    next_c_idx = (c_idx + 1) % L
    next_d_idx = d_idx
    nx, ny = x, y
    if commands[c_idx] == 'S':
        nx, ny = x + dx[d_idx], y + dy[d_idx]

        if not (0 <= nx < N and 0 <= ny < M) or field[nx][ny] == 'X':
            nx, ny = x, y
    elif commands[c_idx] == 'L':
        next_d_idx = (d_idx + 1) % 4
    else:
        next_d_idx = (d_idx - 1) % 4

    if not visited[nx][ny][next_c_idx][next_d_idx]:
        result[x][y][c_idx][d_idx] = dfs(nx, ny, next_c_idx, next_d_idx)
    else:
        result[x][y][c_idx][d_idx] = result[nx][ny][next_c_idx][next_d_idx]

    return result[x][y][c_idx][d_idx]


while True:
    try:
        N, M = map(int, input().split())

        field = [list(input().rstrip()) for _ in range(N)]

        L = int(input())

        commands = input().rstrip()
        start_point = 0
        ans = 0
        visited = [[[[False] * 4 for _ in range(L)] for _ in range(M)] for _ in range(N)]
        result = [[[[False] * 4 for _ in range(L)] for _ in range(M)] for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if field[i][j] == 'X':
                    continue
                start_point += 1
                ans += dfs(i, j, 0, 0)

        if ans == start_point:
            print('OK')
        else:
            print(ans)
    except:
        break
