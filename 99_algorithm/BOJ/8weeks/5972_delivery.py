import sys, heapq
# from collections import defaultdict

input = sys.stdin.readline


def dijkstra(graph, start, end):
    queue = [(0, start)]
    distances = [float('inf') for _ in range(N + 1)]
    distances[start] = 0

    while queue:
        curr_distance, curr_node = heapq.heappop(queue)
        if curr_distance > distances[curr_node]:
            continue

        for next_node, weight in graph[curr_node]:
            # print(next_node, weight)
            if (distance := curr_distance + weight) < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(queue, (distance, next_node))

    return distances[end]


N, M = map(int, input().split())

adj = [list() for _ in range(N + 1)]

for _ in range(M):
    U, V, P = map(int, input().split())
    adj[U].append((V, P))
    adj[V].append((U, P))
    # adj[U][V] = P
    # adj[V][U] = P

if N == 1:
    print(0)
else:
    print(dijkstra(adj, 1, N))
