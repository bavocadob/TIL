import sys

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
    size[px] += size[py]


N, M, Q = map(int, input().split())

edges = [(0, 0)]

for _ in range(M):
    edges.append(tuple(map(int, input().split())))

parents = [i for i in range(N + 1)]
size = [1] * (N + 1)
queries = []
visited = [False] * (M + 1)

for _ in range(Q):
    q = int(input())
    queries.append(q)
    visited[q] = True

for i in range(1, M + 1):
    if visited[i]:
        continue
    a, b = edges[i]
    union(a, b)

ans = 0

while queries:
    q = queries.pop()
    a, b = edges[q]
    pa = find(a)
    pb = find(b)
    if pa == pb:
        continue
    ans += size[pa] * size[pb]
    union(a, b)

print(ans)
