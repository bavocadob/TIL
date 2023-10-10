import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
INF = int(1e9)


def is_valid(x_, y_):
    return 0 <= x_ < N and 0 <= y_ < M


def solution():
    while queue:
        status, x, y = queue.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if not is_valid(nx, ny) or maze[nx][ny] == '#' or visited[status][nx][ny] != INF:
                continue

            if maze[nx][ny] == '.' or maze[nx][ny] == '0':
                visited[status][nx][ny] = visited[status][x][y] + 1
                queue.append((status, nx, ny))
            elif 'a' <= maze[nx][ny] <= 'f':
                temp = status | (1 << ord(maze[nx][ny]) - ord('a'))
                visited[temp][nx][ny] = visited[status][x][y] + 1
                queue.append((temp, nx, ny))
            elif 'A' <= maze[nx][ny] <= 'F':
                if status & (1 << ord(maze[nx][ny]) - ord('A')):
                    visited[status][nx][ny] = visited[status][x][y] + 1
                    queue.append((status, nx, ny))
            elif maze[nx][ny] == '1':
                return visited[status][x][y] + 1

    return -1


N, M = map(int, input().split())
visited = [[[INF] * M for _ in range(N)] for _ in range(64)]

maze = [input().rstrip() for _ in range(N)]

queue = deque()

end_x = end_y = 0
for i in range(N):
    for j in range(M):
        if maze[i][j] == '0':
            queue.append((0, i, j))
            visited[0][i][j] = 0
        elif maze[i][j] == '1':
            end_x, end_y = i, j

print(solution())
