import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def valid(x, y):
    return 0 <= x < N and 0 <= y < M


def bfs():
    global ans
    stack = set([(0, 0, board[0][0])])

    while stack:
        x, y, curr = stack.pop()
        ans = max(ans, len(curr))
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if valid(nx, ny):
                if board[nx][ny] not in curr:
                    stack.add((nx, ny, curr + board[nx][ny]))


N, M = map(int, input().split())

board = [list(input().rstrip()) for _ in range(N)]

ans = 0
bfs()

print(ans)
