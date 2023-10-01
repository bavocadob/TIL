import copy
import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs():
    global max_virus
    temp_labo = copy.deepcopy(laboratory)
    # virus_visited = [[False] * M for _ in range(N)]

    virus_cnt = len(virus)
    queue = deque()
    for x, y in virus:
        queue.append((x, y))
    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and temp_labo[nx][ny] == 0:
                temp_labo[nx][ny] = 2
                virus_cnt += 1
                queue.append((nx, ny))

        if max_virus <= virus_cnt:
            return
    # print(virus_cnt)
    # print(curr)
    max_virus = min(max_virus, virus_cnt)


def backtrack(depth, idx):
    if depth == 3:
        bfs()
        return

    for i in range(idx, len(candidate)):
        if not visited[i]:
            visited[i] = True
            laboratory[candidate[i][0]][candidate[i][1]] = 1
            backtrack(depth + 1, idx + 1)
            visited[i] = False
            laboratory[candidate[i][0]][candidate[i][1]] = 0


N, M = map(int, input().split())

laboratory = [list(map(int, input().split())) for _ in range(N)]

candidate = []
virus = []
wall_cnt = 3
for i in range(N):
    for j in range(M):
        if laboratory[i][j] == 0:
            candidate.append((i, j))
        else:
            if laboratory[i][j] == 2:
                virus.append((i, j))
            else:
                wall_cnt += 1

max_virus = int(1e9)
visited = [False] * len(candidate)

backtrack(0, 0)
print(N * M - wall_cnt - max_virus)
