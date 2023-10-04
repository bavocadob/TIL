import sys

input = sys.stdin.readline


def find(idx):
    if parents[idx] == idx:
        return idx

    parents[idx] = find(parents[idx])

    return parents[idx]


def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa == pb:
        return

    if pa < pb:
        pa, pb = pb, pa

    parents[pb] = pa


N, M = map(int, input().split())

parents = [i for i in range(N + 1)]

for _ in range(M):
    c, a, b = map(int, input().split())
    if c:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
    else:
        union(a, b)
