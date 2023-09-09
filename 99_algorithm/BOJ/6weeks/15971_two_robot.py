import sys

sys.setrecursionlimit(9999999)

input = sys.stdin.readline


def dfs(idx, route):
    global result
    if result:
        return

    if idx == end:
        result = sum(route) - max(route)
        return

    for next_node, distance in connection[idx]:
        if not visited[next_node]:
            visited[next_node] = True
            route.append(distance)
            dfs(next_node, route)
            route.pop()


N, start, end = map(int, input().split())

if N > 2 and start != end:

    connection = [list() for _ in range(N + 1)]
    visited = [False] * (N + 1)

    for _ in range(N - 1):
        x, y, d = map(int, input().split())
        connection[x].append((y, d))
        connection[y].append((x, d))

    r = []
    result = 0

    visited[start] = True

    stack = [start]
    dfs(start, r)
    print(result)
else:
    print(0)
