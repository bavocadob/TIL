from collections import deque
import sys

input = sys.stdin.readline

N, K, D = map(int, input().split())

S = 0
T = N + D + 1

F = [[0] * (T + 1) for _ in range(T + 1)]
C = [[0] * (T + 1) for _ in range(T + 1)]

food_capacity = list(map(int, input().split()))

adj = [list() for _ in range(T + 1)]

for i in range(D):
    C[i + N + 1][T] = food_capacity[i]
    adj[i + N + 1].append(T)
    adj[T].append(i + N + 1)

for i in range(N):
    _, *foods = map(int, input().split())
    for food in foods:
        adj[i + 1].append(food + N)
        adj[food + N].append(i + 1)
        C[i + 1][food + N] = 1
    adj[S].append(i + 1)
    adj[i + 1].append(S)
    C[S][i + 1] = K

ans = 0

while True:
    parent = [-1] * (T + 1)
    parent[S] = S
    queue = deque([S])

    while queue:
        curr = queue.popleft()

        for next_node in adj[curr]:
            if parent[next_node] == -1 and C[curr][next_node] - F[curr][next_node] > 0:
                parent[next_node] = curr
                queue.append(next_node)

    # print(parent)
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
