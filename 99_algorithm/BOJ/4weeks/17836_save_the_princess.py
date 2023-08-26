import sys

from collections import deque

input = sys.stdin.readline

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def solution(visited):
    queue = deque([(0, 0, False)])

    while queue:
        x, y, gramr = queue.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            # 성 범위 일때
            if 0 <= nx < N and 0 <= ny < M:
                # 그람먹은 경우
                if gramr:
                    if visited[1][nx][ny] == 99999:
                        visited[1][nx][ny] = visited[1][x][y] + 1
                        queue.append((nx, ny, True))
                # 그람 안 먹은 경우
                else:
                    if visited[0][nx][ny] == 99999:
                        if castle[nx][ny] == 0:
                            visited[0][nx][ny] = visited[0][x][y] + 1
                            queue.append((nx, ny, False))
                        elif castle[nx][ny] == 2:
                            visited[0][nx][ny] = visited[0][x][y] + 1
                            visited[1][nx][ny] = visited[0][x][y] + 1
                            queue.append((nx, ny, True))


N, M, T = map(int, input().split())

castle = [list(map(int, input().split())) for _ in range(N)]

# 0은 그람 먹기전 1은 그람 먹은 후
v = [[[99999] * M for _ in range(N)] for _ in range(2)]
v[0][0][0] = 1

solution(v)

step = min(v[1][N - 1][M - 1], v[0][N - 1][M - 1]) - 1

if step > T:
    print('Fail')
else:
    print(step)