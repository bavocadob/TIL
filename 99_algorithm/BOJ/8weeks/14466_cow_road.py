import sys

from collections import defaultdict


input = sys.stdin.readline


def dfs(x, y):
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 < nx <= N and 0 < ny <= N and area[nx][ny] == -1 and (nx, ny) not in connection[(x, y)]:
            area[nx][ny] = area_idx
            dfs(nx, ny)


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N, K, R = map(int, input().split())

connection = defaultdict(list)

for _ in range(R):
    x1, y1, x2, y2 = map(int, input().split())
    connection[(x1, y1)].append((x2, y2))
    connection[(x2, y2)].append((x1, y1))

area = [[-1] * (N + 1) for _ in range(N + 1)]

area_idx = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if area[i][j] == -1:
            area[i][j] = area_idx
            dfs(i, j)
            area_idx += 1

area_cnt = [0] * area_idx

for _ in range(K):
    i, j = map(int, input().split())
    area_cnt[area[i][j]] += 1

ans = 0
for i in range(area_idx - 1):
    for j in range(i + 1, area_idx):
        ans += area_cnt[i] * area_cnt[j]

print(ans)
