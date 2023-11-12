import sys

input = sys.stdin.readline


def find(idx, parents):
    if parents[idx] == idx:
        return idx

    parents[idx] = find(parents[idx], parents)
    return parents[idx]


def union(x, y, parents):
    px = find(x, parents)
    py = find(y, parents)

    if px == py:
        return

    if px > py:
        px, py = py, px

    parents[py] = px


N, M = map(int, input().split())

adj = []

for _ in range(M + 1):
    u, v, w = map(int, input().split())
    adj.append((w, u, v))

worst = 0
best = N

best_parents = [i for i in range(N + 1)]
worst_parents = [i for i in range(N + 1)]

for i in range(M + 1):
    w, u, v = adj[i]
    if w:
        pa = find(u, best_parents)
        pb = find(v, best_parents)
        if pa != pb:
            best -= 1
            union(u, v, best_parents)
    else:
        pa = find(u, worst_parents)
        pb = find(v, worst_parents)
        if pa != pb:
            worst += 1
            union(u, v, worst_parents)



print(worst ** 2 - best ** 2)
