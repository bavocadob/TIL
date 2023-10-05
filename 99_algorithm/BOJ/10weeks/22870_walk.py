import sys
import heapq

input = sys.stdin.readline

INF = float('inf')


def dijkstra(start):
    distances = [INF] * (N + 1)
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        curr_dist, curr_node = heapq.heappop(queue)

        if distances[curr_node] < curr_dist:
            continue

        for n_node, w in adj[curr_node]:
            if visited[n_node]:
                continue
            distance = curr_dist + w
            if distances[n_node] > distance:
                distances[n_node] = distance
                heapq.heappush(queue, (distance, n_node))

    return distances


N, M = map(int, input().split())

adj = [list() for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

for i in range(1, N + 1):
    adj[i].sort()

S, E = map(int, input().split())
visited = [False] * (N + 1)

s_to_e = dijkstra(E)

route_node = S
route_cost = 0
while route_node != E:
    for next_node, weight in adj[route_node]:
        if route_cost + weight + s_to_e[next_node] == s_to_e[S]:
            visited[next_node] = True
            route_cost += weight
            route_node = next_node
            break

# print(visited)

e_to_s = dijkstra(E)
# print(s_to_e)
# print(e_to_s)

print(s_to_e[S] + e_to_s[S])
