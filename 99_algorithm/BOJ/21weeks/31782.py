import sys
from collections import deque

input = sys.stdin.readline


def calc(a, b):
    aa, bb = a, b

    while aa < N and A[aa][b] == 'O':
        aa += 1

    while bb < M and A[a][bb] == 'O':
        bb += 1

    h = aa - a
    w = bb - b

    for i in range(a, aa):
        for j in range(b, bb):
            visited[i][j] = True

    if min(h, w) <= K:
        return 0
    else:
        return h * w


dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

N, M, K = map(int, input().split())

A = [list(input()) for _ in range(N)]

queue = deque()

for i in range(N):
    for j in range(M):
        if A[i][j] == 'O':
            queue.append((i, j))

while queue:
    x, y = queue.popleft()

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]

        if 0 <= nx < N and 0 <= ny < M and A[nx][ny] == '.':
            cnt = 0
            for kk in range(4):
                nnx, nny = nx + dx[kk], ny + dy[kk]
                if 0 <= nnx < N and 0 <= nny < M and A[nnx][nny] == 'O':
                    cnt += 1

            if cnt >= 2:
                A[nx][ny] = 'O'
                queue.append((nx, ny))

visited = [[False] * M for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            ans += calc(i, j)

print(ans)
