import sys
from collections import deque

input = sys.stdin.readline

INF = int(1e9)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(virus_idx):
    queue = deque()
    visited = [[0] * N for _ in range(N)]

    for v_idx in virus_idx:
        x, y = viruses[v_idx]
        visited[x][y] = 1
        queue.append((x, y))
    v_cnt = 0
    time = 1
    while queue:
        x, y = queue.popleft()
        if laboratory[x][y] == 0:
            time = visited[x][y]
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and laboratory[nx][ny] != 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                if laboratory[nx][ny] == 0:
                    v_cnt += 1

    if v_cnt == no_virus_cnt:
        return time - 1
    else:
        return INF


def dfs(depth, idx, virus_idx: list):
    if depth == M:
        return bfs(virus_idx)

    cnt = INF
    for i in range(idx, len(viruses)):
        virus_idx.append(i)
        cnt = min(dfs(depth + 1, i + 1, virus_idx), cnt)
        virus_idx.pop()

    return cnt


def solution():
    return dfs(0, 0, [])


N, M = map(int, input().split())

laboratory = [list(map(int, input().split())) for _ in range(N)]

viruses = []
no_virus_cnt = 0

for i in range(N):
    for j in range(N):
        if laboratory[i][j] == 2:
            viruses.append((i, j))
        elif laboratory[i][j] == 0:
            no_virus_cnt += 1

if no_virus_cnt == 0:
    print(0)
else:
    rst = solution()
    if rst != INF:
        print(rst)
    else:
        print(-1)
