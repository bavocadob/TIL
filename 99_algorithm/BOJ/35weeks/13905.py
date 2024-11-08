import heapq
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

S, E = map(int, input().split())

adj = [list() for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

INF = int(1e9)
queue = [(-INF, S)]

dp = [-1] * (N + 1)
dp[S] = INF
while queue:
    val, node = heapq.heappop(queue)

    if dp[node] != -val:
        continue

    if node == E:
        print(-val)
        break

    for next_node, cost in adj[node]:
        next_cost = min(cost, -val)
        if dp[next_node] >= next_cost:
            continue

        dp[next_node] = next_cost
        heapq.heappush(queue, (-next_cost, next_node))

if dp[E] == -1:
    print(0)
