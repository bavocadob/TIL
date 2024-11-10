import sys

input = sys.stdin.readline


def find(x, parents):
    if parents[x] == x:
        return x

    parents[x] = find(parents[x], parents)
    return parents[x]


def union(x, y, parents):
    px, py = find(x, parents), find(y, parents)

    if px == py:
        return

    parents[py] = px


N, M = map(int, input().split())

connection = []

for _ in range(M):
    a, b = map(int, input().split())

    if a == 1 or b == 1:
        continue

    if a > b:
        a, b = b, a

    connection.append((a - 1, b - 1))

adj = []

input()

for i in range(1, N - 1):
    roads = list(map(int, input().split()))
    for j in range(i + 1, N):
        adj.append((roads[j], i, j))

adj.sort()

ans_cost = 0

parent = [i for i in range(N)]
cnt = 0

rst = []
for a, b in connection:
    if find(a, parent) != find(b, parent):
        union(a, b, parent)
        cnt += 1

for cost, a, b in adj:
    if find(a, parent) == find(b, parent):
        continue

    ans_cost += cost

    union(a, b, parent)
    cnt += 1
    rst.append((a + 1, b + 1))
    if cnt == N - 2:
        break

print(ans_cost, len(rst))
for a, b in rst:
    print(a, b)
