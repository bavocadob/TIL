import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N and not visited[x][y]


def solution(x, y, weakness):
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if is_valid(nx, ny):
            if picture[nx][ny] == picture[x][y]:
                visited[nx][ny] = True
                solution(nx, ny, weakness)
            elif weakness:
                if (picture[x][y] == 'G' and picture[nx][ny] == 'R') or (
                        picture[x][y] == 'R' and picture[nx][ny] == 'G'):
                    visited[nx][ny] = True
                    solution(nx, ny, weakness)


N = int(input())

picture = [list(input()) for _ in range(N)]

visited = [[False] * N for _ in range(N)]

normal_cnt = 0
weakness_cnt = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            solution(i, j, False)
            normal_cnt += 1

visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            solution(i, j, True)
            weakness_cnt += 1

print(normal_cnt, weakness_cnt)
