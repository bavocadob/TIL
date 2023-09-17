import sys

sys.setrecursionlimit(99999)

input = sys.stdin.readline


def dfs(idx):
    global max_distance
    for delivery in connection[idx]:
        next_idx, w = delivery

        if distance[next_idx] == -1:
            distance[next_idx] = distance[idx] + w
            max_distance += w
            dfs(next_idx)


N = int(input())

to_campus = []

for _ in range(N + 1):
    to_campus.append(int(input()))

connection = [list() for _ in range(N + 1)]

for _ in range(N):
    x, y, d = map(int, input().split())
    connection[x].append((y, d))
    connection[y].append((x, d))

max_distance = 0

distance = [-1] * (N + 1)
distance[0] = 0
dfs(0)
max_distance *= 2

ans = max_distance + to_campus[0]

for i in range(1, N + 1):
    ans = min(ans, max_distance - distance[i] + to_campus[i])

# print(distance)
# print(to_campus)
print(ans)
