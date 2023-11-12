import sys

input = sys.stdin.readline


def find(idx):
    if parents[idx] == idx:
        return idx

    parents[idx] = find(parents[idx])
    return parents[idx]


def union(x, y):
    px = parents[x]
    py = parents[y]
    if px == py:
        return

    if px > py:
        px, py = py, px

    parents[py] = px


N, M = map(int, input().split())

univ = input().rstrip().split()
parents = [i for i in range(N + 1)]

adj = []

for _ in range(M):
    u, v, w = map(int, input().split())
    adj.append((w, u, v))

adj.sort()
ans = 0
cnt = 0
for w, u, v in adj:
    if univ[u - 1] == univ[v - 1]:
        continue

    pa = find(u)
    pb = find(v)

    if pa != pb:
        union(u, v)
        ans += w
        cnt += 1

        if cnt == N - 1:
            break

if cnt == N - 1:
    print(ans)
else:
    print(-1)
