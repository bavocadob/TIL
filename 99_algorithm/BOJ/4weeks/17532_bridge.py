import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(idx):
    for next_node in connection[idx]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node)


N = int(input())

if N == 2:
    print(1, 2)
else:

    connection = [list() for _ in range(N + 1)]
    visited = [False] * (N + 1)
    for _ in range(N - 2):
        x, y = map(int, input().split())
        connection[x].append(y)
        connection[y].append(x)

    for i in range(1, N + 1):
        if connection[i]:
            visited[i] = True
            dfs(i)
            break

    print(visited.index(False, 1), visited.index(True, 1))
