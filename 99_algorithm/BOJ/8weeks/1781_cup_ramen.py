import sys

sys.setrecursionlimit(9999999)
input = sys.stdin.readline


def find(idx):
    if parent[idx] == idx:
        return idx
    parent[idx] = find(parent[idx])
    return parent[idx]


N = int(input())

ramen = list()
parent = [i for i in range(N + 1)]
for _ in range(N):
    ramen.append(tuple(map(int, input().split())))

ramen.sort(key=lambda x: -x[1])

ans = 0
for d, r in ramen:
    if nd := find(d):
        ans += r
        parent[nd] = nd - 1

print(ans)
