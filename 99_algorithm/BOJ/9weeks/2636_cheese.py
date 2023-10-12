import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


def solution():
    visited = [[False] * M for _ in range(N)]
    queue = deque([(0, 0)])
    cheese_queue = deque()
    last_size = int(1e9)
    time = 0
    while True:

        while queue:
            x, y = queue.popleft()

            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if pan[nx][ny] == 0:
                        queue.append((nx, ny))
                    else:
                        cheese_queue.append((nx, ny))

        if cheese_queue:
            time += 1
            last_size = len(cheese_queue)
            queue = cheese_queue
            cheese_queue = deque()
        else:
            return time, last_size


N, M = map(int, input().split())

pan = [list(map(int, input().split())) for _ in range(N)]

t, s = solution()
print(t)
print(s)
