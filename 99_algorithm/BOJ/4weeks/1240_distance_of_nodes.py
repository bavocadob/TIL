import sys

input = sys.stdin.readline

def dfs(idx, val):
    for c in connection[idx]:
        next_idx, distance = c
        if not visited[next_idx]:
            visited[next_idx] = val + distance
            dfs(next_idx, val + distance)


N, M = map(int, input().split())

connection = [list() for _ in range(N + 1)]

for _ in range(N - 1):
    x, y, d = map(int, input().split())

    connection[x].append((y, d))
    connection[y].append((x, d))

for _ in range(M):
    x, y = map(int, input().split())
    visited = [0] * (N + 1)
    visited[x] = 1
    dfs(x, 0)

    print(visited[y])
