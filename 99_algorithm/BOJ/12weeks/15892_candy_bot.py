import sys
from collections import deque

input = sys.stdin.readline

INF = int(1e9)
N, M = map(int, input().split())

S = 1
T = N

adj = [list() for _ in range(N + 1)]
C = [[0] * (N + 1) for _ in range(N + 1)]
F = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
    C[a][b] += c
    C[b][a] += c


ans = 0

while True:
    prev = [-1] * (N + 1)
    queue = deque([S])
    prev[S] = S

    while queue:
        now = queue.popleft()
        if now == T:
            break

        for next_node in adj[now]:
            if prev[next_node] == -1 and C[now][next_node] - F[now][next_node] > 0:
                prev[next_node] = now
                queue.append(next_node)

    if prev[T] == -1:
        break

    now = T
    min_flow = INF
    while now != S:
        min_flow = min(min_flow, C[prev[now]][now] - F[prev[now]][now])
        now = prev[now]

    now = T

    while now != S:
        F[prev[now]][now] += min_flow
        F[now][prev[now]] -= min_flow
        now = prev[now]

    ans += min_flow

print(ans)
