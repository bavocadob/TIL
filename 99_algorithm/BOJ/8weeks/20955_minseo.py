import sys

input = sys.stdin.readline


def find(idx):
    if parent[idx] == idx:
        return idx
    parent[idx] = find(parent[idx])
    return parent[idx]


def union(x, y):
    global ans
    px = find(x)
    py = find(y)
    if px == py:
        ans += 1

    if px < py:
        parent[py] = px
    else:
        parent[px] = py


N, M = map(int, input().split())

ans = 0
parent = [i for i in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    union(x, y)

union_set = set()
for i in range(1, N + 1):
    union_set.add(find(i))

print(ans + len(union_set) - 1)
