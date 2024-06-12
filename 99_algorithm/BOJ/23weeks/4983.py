import sys


input = sys.stdin.readline
dx = [0, -1, 1, 0]
dy = [1, 0, 0, -1]


def dfs(x, y, depth, field):
    global ans
    if depth > 10:
        return

    for k in range(4):
        nx, ny = x, y
        while 0 <= nx < N and 0 <= ny < M and field[nx][ny] == 0:
            nx += dx[k]
            ny += dy[k]

        if not (0 <= nx < N and 0 <= ny < M):
            continue

        if field[nx][ny] == 3:
            ans = min(ans, depth)
        elif field[nx][ny] == 1:
            if nx == x + dx[k] and ny == y + dy[k]:
                continue

            field[nx][ny] = 0
            dfs(nx - dx[k], ny - dy[k], depth + 1, field)
            field[nx][ny] = 1


INF = int(1e9)

while True:
    M, N = map(int, input().split())

    if N == 0 and M == 0:
        break

    A = [list(map(int, input().split())) for _ in range(N)]

    start_x = start_y = 0
    for i in range(N):
        for j in range(M):
            if A[i][j] == 2:
                start_x, start_y = i, j
                A[i][j] = 0

    ans = INF
    dfs(start_x, start_y, 1, A)
    if ans != INF:
        print(ans)
    else:
        print(-1)
