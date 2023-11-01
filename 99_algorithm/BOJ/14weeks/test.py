block = [[(0, 0), (0, 1), (1, 0)], [(0, 0), (1, 0), (1, -1)], [(0, 0), (0, 1), (1, 1)], [(0, 0), (1, 0), (1, 1)]]


def valid(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


def add_block(x, y, n, m, d, board):
    for dx, dy in block[d]:
        nx, ny = x + dx, y + dy
        if not valid(nx, ny, n, m) or board[nx][ny] == '#':
            return False

    for dx, dy in block[d]:
        nx, ny = x + dx, y + dy
        board[nx][ny] = '#'
    return True


def remove_block(x, y, d, board):
    for dx, dy in block[d]:
        nx, ny = x + dx, y + dy
        board[nx][ny] = '.'


def check(board, n, m):
    for i in range(n):
        for j in range(m):
            if board[i][j] == '.':
                return i, j
    return -1, -1


def dfs(board, n, m):
    i, j = check(board, n, m)

    if i == -1 and j == -1:
        return 1

    rst = 0
    for k in range(4):
        if add_block(i, j, n, m, k, board):
            rst += dfs(board, n, m)
            remove_block(i, j, k, board)
    return rst


def solution():
    n, m = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(n)]

    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == '.':
                cnt += 1

    if not cnt:
        return 1
    elif cnt % 3:
        return 0
    else:
        return dfs(board, n, m)


T = int(input())

for tc in range(T):
    print(solution())
