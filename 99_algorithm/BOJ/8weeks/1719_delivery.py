from collections import defaultdict
import sys, heapq

input = sys.stdin.readline


def dijkstra(start):
    distances = [float('inf') for _ in range(N + 1)]
    prev = [-1] * (N + 1)
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        curr_distance, curr_node = heapq.heappop(queue)

        if curr_distance != distances[curr_node]:
            continue

        for next_node, weight in adj[curr_node].items():
            if (distance := curr_distance + weight) < distances[next_node]:
                distances[next_node] = distance
                prev[next_node] = curr_node
                heapq.heappush(queue, (distance, next_node))

    for i in range(1, N + 1):
        if i == start:
            continue
        result[i][start] = prev[i]


N, M = map(int, input().split())

adj = defaultdict(dict)

for _ in range(M):
    a, b, p = map(int, input().split())
    adj[a][b] = p
    adj[b][a] = p

result = [['-'] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    dijkstra(i)

for r in result[1:]:
    print(*r[1:])
