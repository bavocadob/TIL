import sys
from collections import deque

input = sys.stdin.readline


def dfs(code, code_idx, x, y):
    visited[x][y] = True

    if code_idx == len(code):
        return

    if code[code_idx] == 'u':
        x -= 1
    elif code[code_idx] == 'd':
        x += 1
    elif code[code_idx] == 'l':
        y -= 1
    elif code[code_idx] == 'r':
        y += 1

    dfs(code, code_idx + 1, x, y)


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y):
    cnt = 1

    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1

    return cnt >= size


T = int(input())

for t in range(1, T + 1):
    H, W, size, N = map(int, input().split())

    visited = [[False] * W for _ in range(H)]

    for _ in range(N):
        temp = input().rstrip()

        dfs(temp, 0, H - 1, 0)

    ans = 0
    for i in range(H):
        for j in range(W):
            if not visited[i][j]:
                if bfs(i, j):
                    ans += 1

    print(f'Data Set {t}:')
    print(ans)
    print()
