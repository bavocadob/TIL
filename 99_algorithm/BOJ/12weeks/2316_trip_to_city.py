import sys
from collections import deque

input = sys.stdin.readline

INF = int(1e9)
N, M = map(int, input().split())
S = 1 + N
T = 2

adj = [list() for _ in range(N * 2 + 1)]
# 1 ~ N == IN  N + 1 ~ 2N == OUT
# N + (1 ~ N)

C = [[0] * (N * 2 + 1) for _ in range(N * 2 + 1)]
F = [[0] * (N * 2 + 1) for _ in range(N * 2 + 1)]

for i in range(1, N + 1):
    adj[i].append(i + N)  # self in -> self out
    C[i][i + N] = 1

for _ in range(M):
    a, b = map(int, input().split())
    adj[a + N].append(b)  # A OUT -> B IN
    adj[b + N].append(a)  # B OUT -> A IN
    adj[a].append(b + N)  # A IN -> B OUT
    adj[b].append(a + N)  # B IN -> A OUT
    C[a + N][b] = 1
    C[b + N][a] = 1

ans = 0

while True:

    prev = [-1] * (N * 2 + 1)
    prev[S] = S
    queue = deque([S])

    while queue and prev[T] == -1:
        now = queue.popleft()

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
