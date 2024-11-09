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

    if px < py:
        px, py = py, px

    parents[py] = px


N = int(input())
parents = [i for i in range(N + 1)]
# adj = [list() for _ in range(N + 1)]
adj = []

ans = 0
for i in range(N):
    roads = list(map(int, input().split()))

    for j in range(i + 1, N):
        if roads[j] < 0:
            union(i + 1, j + 1)
            ans -= roads[j]
        else:
            adj.append((roads[j], i + 1, j + 1))
adj.sort()
ans_cnt = 0
rst = []
for cost, a, b in adj:
    if find(a) == find(b):
        continue

    ans += cost
    ans_cnt += 1
    rst.append((a, b))
    union(a, b)

print(ans, ans_cnt)
for a, b in rst:
    print(a, b)
