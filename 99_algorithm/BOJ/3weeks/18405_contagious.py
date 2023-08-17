import sys
input = sys.stdin.readline

from collections import deque

N, K = map(int, input().split())

test_tube = []
start_point = []

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] != 0:
            start_point.append((temp[j], i, j))

    test_tube.append(temp)

s, x_index, y_index = map(int, input().split())

start_point.sort()
queue = deque(start_point)
queue2 = deque()
day = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while queue and day < s:
    level, x, y = queue.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < N and test_tube[nx][ny] == 0:
            test_tube[nx][ny] = level
            queue2.append((level, nx, ny))

    if not queue:
        queue = queue2
        queue2 = deque()
        day += 1

print(test_tube[x_index - 1][y_index - 1])
