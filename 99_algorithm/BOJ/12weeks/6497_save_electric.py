import sys

input = sys.stdin.readline
sys.setrecursionlimit(999999)


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


while True:
    N, M = map(int, input().split())

    if N == M == 0:
        break

    base_cost = 0
    parents = [i for i in range(N)]
    adj = []

    for _ in range(M):
        a, b, c = map(int, input().split())
        base_cost += c
        adj.append((c, a, b))

    adj.sort()

    min_cost = 0

    for cost, a, b in adj:
        pa = find(a)
        pb = find(b)
        if pa == pb:
            continue

        union(a, b)
        min_cost += cost

    print(base_cost - min_cost)
