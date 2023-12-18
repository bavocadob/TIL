import sys

input = sys.stdin.readline
sys.setrecursionlimit(999999)

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
parents = [i for i in range(N + 1)]

adj = []

for _ in range(M):
    a, b, c, t = map(int, input().split())

    adj.append((c, t, a, b))

adj.sort()
time = 0
cost = 0
cnt = 1

for c, t, a, b in adj:
    if find(a) != find(b):
        union(a, b)
        cost += c
        time = max(t, time)
        cnt += 1
        if cnt == N:
            break

if cnt == N:
    print(time, cost)
else:
    print(-1)
