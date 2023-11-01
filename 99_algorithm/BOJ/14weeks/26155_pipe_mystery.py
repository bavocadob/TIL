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


N, M = map(int, input().split())
parents = [i for i in range(N + 1)]
adj = []

for _ in range(M):
    u, v, w = map(float, input().split())
    u = int(u)
    v = int(v)
    adj.append((w, u, v))

Q = int(input())
queries = []
ans = [0] * Q

for i in range(Q):
    query = float(input())
    queries.append((query, i))

adj.sort(reverse=True)
queries.sort(reverse=True)

union_cnt = 0

adj_idx = 0

for i in range(Q):
    query = queries[i][0]
    while adj_idx < M and adj[adj_idx][0] >= query:
        u = adj[adj_idx][1]
        v = adj[adj_idx][2]
        pu = find(u)
        pv = find(v)
        if pu != pv:
            union_cnt += 1
            union(u, v)
        adj_idx += 1

    ans[queries[i][1]] = N - union_cnt

for a in ans:
    print(a)
