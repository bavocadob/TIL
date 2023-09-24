import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline
INF = float('inf')


def dijkstra(start, end):
    distances = [INF] * (N + 1)
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        curr_distance, curr_node = heapq.heappop(queue)

        if curr_distance != distances[curr_node]:
            continue

        for next_node, weight in adj[curr_node].items():
            if (distance := curr_distance + weight) < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(queue, (distance, next_node))

    return distances[end]


def add_adj(a, b, c):
    if b not in adj[a]:
        adj[a][b] = c
        adj[b][a] = c
    else:
        if adj[a][b] > c:
            adj[a][b] = c
            adj[b][a] = c


def print_route(start, end):
    minimum_cost = dijkstra(start, end)
    if minimum_cost == INF:
        print(-1)
    else:
        print(minimum_cost)


N, M = map(int, input().split())

adj = defaultdict(dict)

for _ in range(M):
    code, *data = map(int, input().split())
    if code:
        add_adj(*data)
    else:
        print_route(*data)
