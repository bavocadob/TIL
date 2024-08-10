import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

from collections import deque

N = int(input())

S = tuple(map(int, input().split()))
S = (S[0] - 1, S[1] - 1, S[2] - 1)
E = tuple(map(int, input().split()))
E = (E[0] - 1, E[1] - 1, E[2] - 1)

A = []

for i in range(N):
    temp = []
    for j in range(N):
        temp_input = input().rstrip()
        temp_2 = []

        for k in range(N):
            temp_2.append(int(temp_input[k]))
        temp.append(temp_2)

    A.append(temp)

visited = [[[0] * N for _ in range(N)] for _ in range(N)]

visited[S[2]][S[0]][S[1]] = 1

queue = deque()

queue.append(S)

while queue:
    x, y, z = queue.popleft()

    if (x, y, z) == E:
        break

    for k in range(6):
        nx, ny, nz = x + dx[k], y + dy[k], z + dz[k]

        if not (0 <= nx < N and 0 <= ny < N and 0 <= nz < N) or visited[nz][nx][ny] > 0 or A[nz][nx][ny] == 1:
            continue

        visited[nz][nx][ny] = visited[z][x][y] + 1
        queue.append((nx, ny, nz))

print(visited[E[2]][E[0]][E[1]] - 1)
