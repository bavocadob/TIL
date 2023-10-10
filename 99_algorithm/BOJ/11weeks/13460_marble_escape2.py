import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def is_valid(x, y):
    return 0 <= x < N and 0 <= y < M


def move_marble(x, y, d):
    cnt = 0

    while True:
        if maze[x][y] == 'O':
            break

        nx, ny = x + dx[d], y + dy[d]
        if not is_valid(nx, ny) or maze[nx][ny] == '#':
            break
        x, y = nx, ny
        cnt += 1
    return (x, y, cnt)


def solution():
    ans = 0

    while queue:
        bx, by, rx, ry = queue.popleft()
        c = visited[bx][by][rx][ry]
        for k in range(4):
            nbx, nby, bc = move_marble(bx, by, k)
            nrx, nry, rc = move_marble(rx, ry, k)

            if maze[nbx][nby] == 'O':
                continue

            if maze[nrx][nry] == 'O':
                return c + 1

            if nrx == nbx and nry == nby:
                if bc > rc:
                    nbx, nby = nbx - dx[k], nby - dy[k]
                else:
                    nrx, nry = nrx - dx[k], nry - dy[k]

            if not visited[nbx][nby][nrx][nry]:
                visited[nbx][nby][nrx][nry] = c + 1
                queue.append((nbx, nby, nrx, nry))
    return -1


N, M = map(int, input().split())

visited = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

maze = [list(input().rstrip()) for _ in range(N)]

blue_x = blue_y = red_x = red_y = 0

for i in range(N):
    for j in range(M):
        if maze[i][j] == 'R':
            red_x, red_y = i, j
        elif maze[i][j] == 'B':
            blue_x, blue_y = i, j

queue = deque([(blue_x, blue_y, red_x, red_y)])

result = solution()
if result > 10:
    print(-1)
else:
    print(result)
