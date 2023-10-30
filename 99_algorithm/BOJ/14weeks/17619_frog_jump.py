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


N, Q = map(int, input().split())

logs = []

for i in range(1, N + 1):
    x1, x2, _ = map(int, input().split())

    logs.append((x1, x2, i))

parents = [i for i in range(N + 1)]

logs.sort()

# l = 0
r = -1
curr = 0
for left, right, node in logs:
    if left <= r:
        union(curr, node)
        curr = find(node)
        r = max(r, right)
        # l = min(l, left)
    else:
        curr = node
        r = right

for _ in range(Q):
    u, v = map(int, input().split())
    if find(u) == find(v):
        print(1)
    else:
        print(0)
