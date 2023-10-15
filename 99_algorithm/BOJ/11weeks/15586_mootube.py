import sys

input = sys.stdin.readline


def find(idx):
    if parent[idx] == idx:
        return idx

    parent[idx] = find(parent[idx])
    return parent[idx]


def union(x, y):
    px = find(x)
    py = find(y)

    if px == py:
        return

    if size[py] > size[px]:
        px, py = py, px

    size[px] += size[py]
    parent[py] = px


N, Q = map(int, input().split())

adj = []

for _ in range(N - 1):
    a, b, c = map(int, input().split())
    adj.append((c, a, b))

adj.sort(reverse=True)

ans = [0] * Q
queries = []

for i in range(Q):
    k, v = map(int, input().split())
    queries.append((k, v, i))

queries.sort()

parent = [i for i in range(N + 1)]
size = [1] * (N + 1)

adj_idx = 0

while queries:
    k, v, i = queries.pop()

    while adj_idx < N - 1 and adj[adj_idx][0] >= k:
        c, a, b = adj[adj_idx]
        union(a, b)
        adj_idx += 1

    ans[i] = size[find(v)] - 1

for i in range(Q):
    print(ans[i])
