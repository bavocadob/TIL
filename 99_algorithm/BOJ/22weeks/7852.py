import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def solve(x, y):
    queue = deque()
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True

    queue.append((x, y, 0))
    rst = []
    while queue:
        temp_queue = deque()
        while queue:
            x, y, dist = queue.popleft()

            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if not (0 <= nx < N and 0 <= ny < N) or visited[nx][ny]:
                    continue

                visited[nx][ny] = True
                temp_queue.append((nx, ny, dist + 1))
                if original_map[nx][ny] != 0:
                    rst.append(original_map[nx][ny])

        if len(rst) > 0:
            break

        queue = temp_queue
    if not rst or len(rst) > 1:
        return 0

    return rst[0]


N = int(input())

original_map = [list(map(int, input().split())) for _ in range(N)]

new_map = deepcopy(original_map)

for i in range(N):
    for j in range(N):
        if original_map[i][j] == 0:
            target = solve(i, j)
            new_map[i][j] = target

for nm in new_map:
    print(*nm)
