import sys
import heapq

from collections import defaultdict

input = sys.stdin.readline


def dijkstra(graph, dist, start, end):
    dist[start] = 0
    queue = [(0, start)]
    # queue = deque()
    # queue.append((0, start))

    while queue:
        # print(queue)
        # current_distance, current_node = queue.popleft()
        current_distance, current_node = heapq.heappop(queue)

        if dist[current_node] < current_distance:
            continue

        if current_node == end:
            break

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
                # queue.append((distance, neighbor))


def dijkstra_2(graph, dist, start, end):
    dist[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if dist[current_node] < current_distance:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distances[current_node] + weight + distances_rev[neighbor] == distances[end]:
                continue
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
                # queue.append((distance, neighbor))


while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    S, D = map(int, input().split())

    adj = defaultdict(dict)
    adj_rev = defaultdict(dict)
    for _ in range(M):
        U, V, P = map(int, input().split())
        adj[U][V] = P
        adj_rev[V][U] = P

    distances = [float('inf') for _ in range(N)]
    distances_rev = [float('inf') for _ in range(N)]
    distances_result = [float('inf') for _ in range(N)]
    dijkstra(adj, distances, S, D)
    dijkstra(adj_rev, distances_rev, D, S)
    dijkstra_2(adj, distances_result, S, D)

    if distances_result[D] != float('inf'):
        print(distances_result[D])
    else:
        print(-1)
