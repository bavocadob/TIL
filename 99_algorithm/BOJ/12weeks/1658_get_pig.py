import sys

input = sys.stdin.readline

from collections import deque

INF = int(1e9)

# 돼지우리 수, 사람 수
M, N = map(int, input().split())

# 0 = 시작노드, 1~N = 사람노드, N + 1 ~ N + M = 돼지우리 노드, N + M + 1는 싱크노드
S = 0
T = N + M + 1

F = [[0] * (T + 1) for _ in range(T + 1)]
C = [[0] * (T + 1) for _ in range(T + 1)]

adj = [list() for _ in range(T + 1)]

base_pig = list(map(int, input().split()))

key_owners = [list() for _ in range(M + 1)]

for i in range(M):
    C[N + 1 + i][T] = base_pig[i]
    adj[N + 1 + i].append(T)
    adj[T].append(N + 1 + i)

for i in range(N):
    key_cnt, *keys, s_to_n = map(int, input().split())
    for key in keys:
        C[1 + i][N + key] = INF
        adj[1 + i].append(N + key)
        adj[N + key].append(i + 1)
        key_owners[key].append(i + 1)

    C[S][1 + i] = s_to_n

    adj[S].append(1 + i)
    adj[1 + i].append(S)

for i in range(1, M + 1):
    for j in range(len(key_owners[i]) - 1):
        for k in range(j + 1, len(key_owners[i])):
            a = key_owners[i][j]
            b = key_owners[i][k]
            C[b][a] = INF
            adj[a].append(b)
            adj[b].append(a)

ans = 0

while True:
    prev = [-1] * (T + 1)
    prev[S] = S
    queue = deque([S])

    while queue:
        now = queue.popleft()

        for next_node in adj[now]:
            if prev[next_node] == -1 and C[now][next_node] - F[now][next_node] > 0:
                prev[next_node] = now
                queue.append(next_node)

    if prev[T] == -1:
        break

    now = T
    flow = INF
    while now != S:
        flow = min(flow, C[prev[now]][now] - F[prev[now]][now])
        now = prev[now]

    now = T

    while now != S:
        F[prev[now]][now] += flow
        F[now][prev[now]] -= flow
        now = prev[now]

    ans += flow

print(ans)
