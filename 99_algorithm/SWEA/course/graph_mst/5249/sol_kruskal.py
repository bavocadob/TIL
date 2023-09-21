T = int(input())


def find(idx):
    if parent[idx] == idx:
        return idx

    parent[idx] = find(parent[idx])
    return parent[idx]


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for tc in range(T):
    V, E = map(int, input().split())

    adj = []
    for _ in range(E):
        x, y, w = map(int, input().split())
        adj.append((w, x, y))
    adj.sort()

    parent = [i for i in range(V + 1)]

    ans = 0

    for w, x, y in adj:
        if find(x) != find(y):
            union(x, y)
            ans += w

    print(f'#{tc + 1} {ans}')
