import sys

input = sys.stdin.readline


def find(x, par):
    if par[x] == x:
        return x

    par[x] = find(par[x], par)
    return par[x]


def union(x, y, par):
    px = find(x, par)
    py = find(y, par)
    if px == py:
        return

    if px > py:
        px, py = py, px

    par[py] = px


def get_mst(idx):
    ans = 0

    parents = [p for p in range(N + 1)]
    cnt = 1

    for j in range(idx, M):
        weight, x, y = adj[j]

        if find(x, parents) != find(y, parents):
            union(x, y, parents)
            cnt += 1
            ans += weight
        if cnt == N:
            break

    if cnt == N:
        return ans
    else:
        return 0


N, M, K = map(int, input().split())

rst = [0] * K

adj = []

for w in range(1, M + 1):
    a, b = map(int, input().split())
    adj.append((w, a, b))

for i in range(K):
    mst = get_mst(i)
    if mst:
        rst[i] = mst
    else:
        break

print(*rst)
