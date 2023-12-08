import sys

input = sys.stdin.readline


def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    px = find(x)
    py = find(y)

    if px == py:
        return

    if x > y:
        x, y = y, x

    parent[py] = px


E, V = map(int, input().split())

parent = [i for i in range(E + 1)]
adj = []

for _ in range(V):
    a, b, c = map(int, input().split())
    adj.append((c, a, b))

adj.sort()

ans = 0

last = 0
for c, a, b in adj:
    if find(a) != find(b):
        ans += c
        union(a, b)
        last = c

print(ans - last)
