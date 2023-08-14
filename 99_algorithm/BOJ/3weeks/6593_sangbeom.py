import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 1, 0, -1, 0, 0]
dy = [1, 0, -1, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while True:
    H, N, M = map(int, input().split())

    if H == N == M == 0:
        break

    building = []

    start_index = None
    end_index = None

    for height in range(H):
        floor = []
        for i in range(N):
            input_str = input().rstrip()
            line = []
            for j in range(M):
                if input_str[j] == '#':
                    line.append(-1)
                elif input_str[j] == '.':
                    line.append(0)
                if input_str[j] == 'S':
                    start_index = (height, i, j)
                    line.append(1)
                elif input_str[j] == 'E':
                    end_index = (height, i, j)
                    line.append(0)
            floor.append(line)
        building.append(floor)
        input()

    queue = deque([start_index])

    while queue:
        z, x, y = queue.popleft()
        if (z, x, y) == end_index:
            break

        for k in range(6):
            nz, nx, ny = z + dz[k], x + dx[k], y + dy[k]
            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M:
                if building[nz][nx][ny] == 0:
                    building[nz][nx][ny] = building[z][x][y] + 1
                    queue.append((nz, nx, ny))

    z, x, y = end_index
    if building[z][x][y] > 0:
        print(f'Escaped in {building[z][x][y] - 1} minute(s).')
    else:
        print('Trapped!')
