# ㄴ ㄱ 역ㄱ 역ㄴ
import sys
input = sys.stdin.readline

dx = [[-1, 0], [0, 1], [0, 1], [-1, 0], [1, 1], [0, -1], [0, 1], [-1, -1], [0, 1], [-1, -1], [1, 1], [0, -1]]
dy = [[0, 1], [-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [1, 1], [-1, 0], [-1, -1], [0, 1], [-1, 0], [1, 1]]


def can_insert(x, y, k):
    for m in range(2):
        nx, ny = x + dx[k][m], y + dy[k][m]
        if not (0 <= nx < N and 0 <= ny < M) or room[nx][ny] == '#':
            return False
    return True


def backtrack(depth):
    global cnt

    if depth == len(floor):
        for nx, ny in floor:
            if room[nx][ny] == '.':
                return
        cnt += 1
        return
    x, y = floor[depth]

    if room[x][y] == '#':
        backtrack(depth + 1)
        return

    room[x][y] = '#'
    for k in range(12):
        if can_insert(x, y, k):
            for m in range(2):
                nx, ny = x + dx[k][m], y + dy[k][m]
                room[nx][ny] = '#'
            backtrack(depth + 1)
            for m in range(2):
                nx, ny = x + dx[k][m], y + dy[k][m]
                room[nx][ny] = '.'

    room[x][y] = '.'


while True:

    N, M = map(int, input().split())
    if (N, M) == (0, 0):
        break
    room = [list(input()) for _ in range(N)]

    floor = []
    cnt = 0
    for i in range(N):
        for j in range(M):
            if room[i][j] == '.':
                floor.append((i, j))

    backtrack(0)

    print(cnt)
