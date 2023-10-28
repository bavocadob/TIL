import sys
from math import hypot

input = sys.stdin.readline


def find(idx):
    if parents[idx] == idx:
        return idx

    parents[idx] = find(parents[idx])
    return parents[idx]


def union(x, y):
    px = find(x)
    py = find(y)

    if px == py:
        return

    if px > py:
        px, py = py, px

    parents[py] = px


N, M = map(int, input().split())

parents = [i for i in range(N + 1)]

gods = [list(map(int, input().split())) for _ in range(N)]

road_cnt = 0

for _ in range(M):
    a, b = map(int, input().split())
    pa = find(a)
    pb = find(b)

    if pa != pb:
        union(a, b)
        road_cnt += 1

queue = []

length = 0.0
for i in range(N - 1):
    for j in range(i + 1, N):
        pa = find(i + 1)
        pb = find(j + 1)

        if pa != pb:
            x1, y1 = gods[i]
            x2, y2 = gods[j]
            h = hypot(x1 - x2, y1 - y2)
            queue.append((h, i + 1, j + 1))

queue.sort()
for h, a, b in queue:
    pa = find(a)
    pb = find(b)

    if pa != pb:
        union(a, b)
        length += h
        road_cnt += 1

print("{:.2f}".format(length))
