import sys

input = sys.stdin.readline

dx = [-1, -1, 1, 1]
dy = [-1, 1, -1, 1]


def is_valid(x, y):
    return 0 <= x < 8 and 0 <= y < 8


def dfs(x, y, root_x, root_y, cnt):
    global ans, ans_x, ans_y
    if cnt > ans:
        ans = cnt
        ans_x, ans_y = root_x, root_y

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]

        if is_valid(nx, ny) and board[nx][ny] == 'B':
            nnx, nny = nx + dx[k], ny + dy[k]
            if is_valid(nnx, nny) and board[nnx][nny] == ' ':
                board[nx][ny] = ' '
                board[x][y] = ' '
                board[nnx][nny] = 'K'
                dfs(nnx, nny, root_x, root_y, cnt + 1)
                board[nx][ny] = 'B'
                board[x][y] = 'K'
                board[nnx][nny] = ' '


N = int(input())

for _ in range(N):

    board = [list(input()) for _ in range(8)]

    ans = ans_x = ans_y = -1

    for i in range(8):
        if len(board[i]) < 8:
            need = 8 - len(board[i])
            for c in range(need):
                board[i].append(' ')

        for j in range(8):
            if board[i][j] == 'K':
                dfs(i, j, i, j, 0)

    print(ans_x, ans_y, ans)
