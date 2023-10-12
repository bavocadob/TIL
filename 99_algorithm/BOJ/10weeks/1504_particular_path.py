import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)


def dijkstra(start):
    distances = [INF] * (N + 1)

    distances[start] = 0

    queue = [(0, start)]

    while queue:
        curr_dist, curr_node = heapq.heappop(queue)

        if distances[curr_node] < curr_dist:
            continue

        for next_node, weight in adj[curr_node]:
            if (distance := curr_dist + weight) < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(queue, (distance, next_node))

    return distances


N, M = map(int, input().split())

adj = [list() for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

u, v = map(int, input().split())
w = 0
for node, weight in adj[u]:
    if node == v:
        w = weight

# 1 -> v -> u -> N
# 1 -> u -> v -> N

from_start = dijkstra(1)
from_u = dijkstra(u)
from_v = dijkstra(v)

ans = min(from_start[v] + from_v[u] + from_u[N], from_start[u] + from_u[v] + from_v[N])
if ans < INF:
    print(ans)
else:
    print(-1)
