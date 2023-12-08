import heapq
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
        return

    if px > py:
        px, py = py, px

    parents[py] = px


v, e = map(int, input().split())

queue = []

parents = [i for i in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    heapq.heappush(queue, (c, a, b))

ans = 0
cnt = 0
while queue:
    cost, a, b = heapq.heappop(queue)
    pa = find(a)
    pb = find(b)

    if pa != pb:
        ans += cost
        union(a, b)
        cnt += 1

        if cnt == v - 1:
            break

print(ans)
