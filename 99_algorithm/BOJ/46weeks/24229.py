import sys

input = sys.stdin.readline
N = int(input())

roads = []

for _ in range(N):
    l, r = map(int, input().split())

    roads.append((l, r))

roads.sort(key=lambda x: (x[0], -x[1]))

start, end = roads[0]

new_roads = []
for i in range(1, N):
    l, r = roads[i]

    if l <= end:
        end = max(end, r)
    else:
        new_roads.append((start, end))
        start, end = l, r
else:
    new_roads.append((start, end))

ans = 0
limit = 0

for l, r in new_roads:
    if l > limit:
        break

    limit = max(limit, r + (r - l))
    ans = max(ans, r)

print(ans)
