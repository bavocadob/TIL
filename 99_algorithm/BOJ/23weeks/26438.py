import sys

input = sys.stdin.readline
sys.setrecursionlimit(999999)


def dfs(node):
    visited[node] = 1

    for next_node in adj[node]:
        if A[node] <= A[next_node]:
            continue

        if not visited[next_node]:
            visited[node] += dfs(next_node)
        else:
            visited[node] += visited[next_node]

    return visited[node]


T = int(input())

for t in range(1, T + 1):
    N = int(input())

    A = list(map(int, input().split()))

    adj = [list() for _ in range(N)]

    for _ in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1

        adj[a].append(b)
        adj[b].append(a)

    visited = [0] * N

    for i in range(N):
        if not visited[i]:
            dfs(i)

    print(f'Case #{t}: {max(visited)}')
