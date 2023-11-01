import sys
from copy import deepcopy

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def find(x, y):
    if parents[x][y] == (x, y):
        return x, y

    parents[x][y] = find(*parents[x][y])

    return parents[x][y]


def union(x1, y1, x2, y2):
    p1 = find(x1, y1)
    p2 = find(x2, y2)

    if p1 == p2:
        return

    if p1[0] * M + p1[1] > p2[0] * M + p2[1]:
        p1, p2 = p2, p1

    parents[p2[0]][p2[1]] = p1
    values[p1[0]][p1[1]] ^= values[p2[0]][p2[1]]


N, M = map(int, input().split())

numbers = [list(map(int, input().split())) for _ in range(N)]

queries = []

parents = [[(i, j) for j in range(M)] for i in range(N)]
values = deepcopy(numbers)
for i in range(N):
    for j in range(M):
        queries.append((numbers[i][j], i, j))

queries.sort(reverse=True)

ans = 0
temp = 0
for v, i, j in queries:
    temp_set = set()
    for k in range(4):
        ni, nj = i + dx[k], j + dy[k]
        if not (0 <= ni < N and 0 <= nj < M) or numbers[ni][nj]:
            continue
        temp_set.add(find(ni, nj))

    for temp_x, temp_y in temp_set:
        temp -= values[temp_x][temp_y]
        union(i, j, temp_x, temp_y)

    parent_x, parent_y = find(i, j)

    temp += values[parent_x][parent_y]
    ans = max(ans, temp)
    numbers[i][j] = 0

print(ans)
