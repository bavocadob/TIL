from collections import defaultdict

import heapq, sys

input = sys.stdin.readline


def dijkstra(graph, start):
    distances = [list() for _ in range(N + 1)]
    distances[start].append(0)
    queue = [(0, start)]

    while queue:
        curr_distance, curr_node = heapq.heappop(queue)

        for next_node, weight in graph[curr_node].items():
            distance = curr_distance + weight

            if len(distances[next_node]) < K:
                heapq.heappush(distances[next_node], -distance)
                heapq.heappush(queue, (distance, next_node))
            else:
                if -distances[next_node][0] > distance:
                    heapq.heappop(distances[next_node])
                    heapq.heappush(distances[next_node], -distance)
                    heapq.heappush(queue, (distance, next_node))

    return distances


N, M, K = map(int, input().split())

adj = defaultdict(dict)

for _ in range(M):
    U, V, P = map(int, input().split())
    adj[U][V] = P

dist = dijkstra(adj, 1)

for i in range(1, N + 1):
    if len(dist[i]) < K:
        print(-1)
    else:
        # print(dist[i])
        print(-heapq.heappop(dist[i]))
