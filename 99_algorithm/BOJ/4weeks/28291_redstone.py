from collections import deque
import sys

input = sys.stdin.readline

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

N, M = map(int, input().split())

block_num = int(input())

circuit = [[0] * M for _ in range(N)]

lamp_lst = []
queue = deque()

visited = [[False] * M for _ in range(N)]

for _ in range(block_num):
    block_type, x, y = input().split()
    x = int(x)
    y = int(y)
    if block_type == 'redstone_block':
        circuit[x][y] = 1
        queue.append((x, y, 15))
        visited[x][y] = True
    elif block_type == 'redstone_dust':
        circuit[x][y] = 2
    elif block_type == 'redstone_lamp':
        circuit[x][y] = 3
        lamp_lst.append((x, y))

while queue:
    x, y, electric = queue.popleft()
    if electric == 0:
        continue

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if circuit[nx][ny] == 2:
                visited[nx][ny] = True
                queue.append((nx, ny, electric - 1))
            elif circuit[nx][ny] == 3:
                visited[nx][ny] = True

success = True
for i in range(len(lamp_lst)):
    if not visited[lamp_lst[i][0]][lamp_lst[i][1]]:
        success = False
        break

if success:
    print('success')
else:
    print('failed')
