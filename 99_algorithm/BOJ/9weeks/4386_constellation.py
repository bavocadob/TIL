import math
import sys

input = sys.stdin.readline

def find(x, y):
    if star_dict[(x, y)] == (x, y):
        return x, y

    star_dict[(x, y)] = find(*star_dict[(x, y)])

    return star_dict[(x, y)]


def union(x1, y1, x2, y2):
    pa = find(x1, y1)
    pb = find(x2, y2)

    if pa == pb:
        return

    star_dict[pb] = pa


N = int(input())

star_dict = dict()
star_lst = []
for _ in range(N):
    a, b = map(float, input().split())
    star_dict[(a, b)] = (a, b)
    star_lst.append((a, b))

queue = []

for i in range(N - 1):
    for j in range(i + 1, N):
        dist = math.hypot(star_lst[i][0] - star_lst[j][0], star_lst[i][1] - star_lst[j][1])
        queue.append((dist, star_lst[i], star_lst[j]))

queue.sort(reverse=True)

ans = 0
cnt = 0

while queue:
    dist, star_a, star_b = queue.pop()
    if find(*star_a) == find(*star_b):
        continue

    ans += dist
    cnt += 1
    union(star_a[0], star_a[1], star_b[0], star_b[1])

    if cnt == N - 1:
        break

print(ans)
