import sys
from collections import deque, defaultdict

input = sys.stdin.readline


def is_valid(x, y):
    return 0 <= x < N + 2 and 0 <= y < M + 2


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    maze = [['.'] * (M + 2)]
    for _ in range(N):
        maze.append(['.'] + list(input()) + ['.'])
    maze.append(['.'] * (M + 2))

    keys = set(input().rstrip().upper())

    queue = deque([(0, 0)])

    candidate = defaultdict(list)
    visited = [[False] * (M + 2) for _ in range(N + 2)]
    ans = 0
    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if not is_valid(nx, ny) or maze[nx][ny] == '*' or visited[nx][ny]:
                continue

            if maze[nx][ny].isupper():
                if maze[nx][ny] in keys:
                    maze[nx][ny] = '.'
                else:
                    candidate[maze[nx][ny]].append((nx, ny))
                    continue
            elif maze[nx][ny].islower():
                key_name = maze[nx][ny].upper()
                keys.add(key_name)
                if key_name in candidate:
                    for nnx, nny in candidate[key_name]:
                        maze[nnx][nny] = '.'
                        visited[nnx][nny] = True
                        queue.append((nnx, nny))
                maze[nx][ny] = '.'
            elif maze[nx][ny] == '$':
                ans += 1
                maze[nx][ny] = '.'

            visited[nx][ny] = True
            queue.append((nx, ny))

    print(ans)
