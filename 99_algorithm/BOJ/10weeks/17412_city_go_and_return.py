import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

adj = [list() for _ in range(N + 1)]

F = [[0] * (N + 1) for _ in range(N + 1)]
C = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    v, e = map(int, input().split())
    adj[v].append(e)
    adj[e].append(v)
    C[v][e] = 1

S = 1
T = 2

ans = 0

while True:
    parent = [-1] * (N + 1)
    parent[S] = S

    queue = deque([S])
    while queue:
        node = queue.popleft()
        for next_node in adj[node]:
            if parent[next_node] == -1 and C[node][next_node] - F[node][next_node] > 0:
                parent[next_node] = node
                queue.append(next_node)

    if parent[T] == -1:
        break

    node = T
    min_flow = int(1e9)
    while node != S:
        min_flow = min(min_flow, C[parent[node]][node] - F[parent[node]][node])
        node = parent[node]

    node = T

    while node != S:
        F[parent[node]][node] += min_flow
        F[node][parent[node]] -= min_flow
        node = parent[node]

    ans += min_flow

print(ans)
