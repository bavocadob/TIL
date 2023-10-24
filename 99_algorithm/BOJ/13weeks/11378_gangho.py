import sys
from collections import deque

input = sys.stdin.readline

INF = int(1e9)
N, M, K = map(int, input().split())

# 2 ~ N + 1 직원
# N + 2 ~ N + M + 1 일거리
# N + M + 2 싱크
root = 0
S1 = 1
S2 = 2
T = N + M + 3

adj = [list() for _ in range(T + 1)]
C = [[0] * (T + 1) for _ in range(T + 1)]
F = [[0] * (T + 1) for _ in range(T + 1)]

adj[root].append(S1)
adj[S1].append(root)
C[root][S1] = N

adj[root].append(S2)
adj[S2].append(root)
C[root][S2] = K

for i in range(3, N + 3):
    _, *jobs = map(int, input().split())
    for job in jobs:
        adj[i].append(job + N + 2)
        adj[job + N + 2].append(i)
        C[i][job + N + 2] = 1

    adj[S1].append(i)
    adj[i].append(S1)
    C[S1][i] = 1

    adj[S2].append(i)
    adj[i].append(S2)
    C[S2][i] = INF

for i in range(N + 3, T):
    adj[i].append(T)
    adj[T].append(i)
    C[i][T] = 1

ans = 0

while True:
    prev = [-1] * (T + 1)
    queue = deque([root])
    prev[root] = root

    while queue:
        now = queue.popleft()
        for next_node in adj[now]:

            if prev[next_node] == -1 and C[now][next_node] - F[now][next_node] > 0:
                prev[next_node] = now
                queue.append(next_node)

    if prev[T] == -1:
        break

    now = T
    min_flow = INF

    while now != root:
        min_flow = min(min_flow, C[prev[now]][now] - F[prev[now]][now])
        now = prev[now]

    now = T

    while now != root:
        F[prev[now]][now] += min_flow
        F[now][prev[now]] -= min_flow
        now = prev[now]

    ans += min_flow

print(ans)
