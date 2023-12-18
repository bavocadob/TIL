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
        return False

    if px > py:
        px, py = py, px

    parents[py] = px
    return True


N, M, t = map(int, input().split())

parents = [i for i in range(N + 1)]
adj = []

for _ in range(M):
    a, b, c = map(int, input().split())
    adj.append((c, a, b))

adj.sort()

bonus = 0

ans = 0

for c, a, b in adj:
    if union(a, b):
        ans += c + bonus
        bonus += t

print(ans)
