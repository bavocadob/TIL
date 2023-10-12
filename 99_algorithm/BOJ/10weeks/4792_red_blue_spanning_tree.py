import sys

input = sys.stdin.readline


def find(parent, idx):
    if parent[idx] == idx:
        return idx

    parent[idx] = find(parent, parent[idx])
    return parent[idx]


def union(parent, x, y):
    px = find(parent, x)
    py = find(parent, y)

    if px == py:
        return

    if py < px:
        px, py = py, px

    parent[py] = px


def mst(plus):
    p = [i for i in range(N + 1)]
    queue = []
    for a, b, c in adj:
        weight = 0
        if c == plus:
            weight += 1
        queue.append((weight, a, b))

    queue.sort(reverse=True)
    size = 0
    result = 0
    while queue:
        w, a, b = queue.pop()
        if find(p, a) == find(p, b):
            continue

        result += w
        size += 1
        union(p, a, b)
        if size == N - 1:
            break
    return result


while True:
    N, M, K = map(int, input().split())

    if not N and not M and not K:
        break

    adj = []

    for _ in range(M):
        color, v, e = input().split()
        v = int(v)
        e = int(e)
        adj.append((v, e, color))

    min_blue = mst('B')
    max_blue = N - 1 - mst('R')
    # print(min_blue, '최저 파랑')
    # print(max_blue, '최대 파랑')

    print(int(min_blue <= K <= max_blue))
