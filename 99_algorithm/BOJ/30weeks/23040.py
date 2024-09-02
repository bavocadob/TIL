import sys

input = sys.stdin.readline


def find(x):
    if parents[x] == x:
        return x

    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    px, py = find(x), find(y)

    if px == py:
        return

    if px > py:
        py, px = px, py

    parents[py] = px

    size[px] += size[py]


N = int(input())

adj = [list() for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(lambda x: int(x) - 1, input().split())
    adj[u].append(v)
    adj[v].append(u)

colours = input().rstrip()

parents = [i for i in range(N + 1)]
size = [1] * (N + 1)
blacks = []

for i in range(N):
    if colours[i] == 'R':
        for next_node in adj[i]:
            if colours[next_node] == 'R':
                union(i, next_node)
    else:
        blacks.append(i)

ans = 0

for black in blacks:
    for next_node in adj[black]:
        if colours[next_node] == 'R':
            ans += size[find(next_node)]

print(ans)
