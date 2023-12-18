import sys

input = sys.stdin.readline


def find(x):
    if parents[x] == x:
        return x

    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    px = find(x)
    py = find(y)

    if px == py:
        return

    if px > py:
        px, py = py, px

    parents[py] = px


N, M = map(int, input().split())

adj = list()
parents = [i for i in range(N + 1)]
max_cost = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    adj.append((c, a, b))
    max_cost += c

adj.sort()

min_cost = 0
cnt = 1

for c, a, b in adj:
    if find(a) != find(b):
        union(a, b)
        cnt += 1
        min_cost += c

print(max_cost - min_cost if cnt == N else -1)
