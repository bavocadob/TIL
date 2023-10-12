import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

adj = [list() for _ in range(N + M + 2)]
S = 0
T = N + M + 1

C = [[0] * (N + M + 2) for _ in range(N + M + 2)]
F = [[0] * (N + M + 2) for _ in range(N + M + 2)]

for i in range(1, N + 1):
    _, *barns = map(int, input().split())
    for barn in barns:
        adj[i].append(barn + N)
        adj[barn + N].append(i)
        C[i][barn + N] = 1
    adj[i].append(S)
    adj[S].append(i)
    C[S][i] = 1

for i in range(N + 1, T):
    adj[i].append(T)
    adj[T].append(i)
    C[i][T] = 1

ans = 0

while True:
    parent = [-1] * (N + M + 2)
    queue = deque([S])
    parent[S] = S

    while queue and parent[T] == -1:
        node = queue.popleft()

        for next_node in adj[node]:
            if C[node][next_node] - F[node][next_node] > 0 and parent[next_node] == -1:
                parent[next_node] = node
                queue.append(next_node)

    if parent[T] == -1:
        break

    node = T
    flow = int(1e9)
    while node != S:
        flow = min(flow, C[parent[node]][node] - F[parent[node]][node])
        node = parent[node]

    node = T

    while node != S:
        F[parent[node]][node] += flow
        F[node][parent[node]] -= flow
        node = parent[node]

    ans += flow

print(ans)
