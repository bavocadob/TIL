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

    if px > py:
        px, py = py, px

    parent[py] = px


N, M = map(int, input().split())

parent = [i for i in range(N)]

ans = 0
for i in range(1, M + 1):
    a, b = map(int, input().split())

    if find(a) != find(b):
        union(a, b)
    else:
        if not ans:
            ans = i

print(ans)
