import sys

input = sys.stdin.readline


def find(node):
    if parents[node] == node:
        return node

    parents[node] = find(parents[node])

    return parents[node]


def union(x, y):
    px, py = find(x), find(y)

    if px == py:
        return

    if px > py:
        px, py = py, px

    parents[py] = px

    size[px] += size[py]


N = int(input())

MAX_SIZE = int(1e6) + 1

parents = [i for i in range(MAX_SIZE)]
size = [1] * MAX_SIZE

for _ in range(N):
    c, *A = input().split()

    A = list(map(int, A))

    if c == 'Q':
        print(size[find(A[0])])
    else:
        union(A[0], A[1])
