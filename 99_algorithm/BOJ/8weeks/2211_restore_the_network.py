import sys

from collections import defaultdict
from heapq import heappop, heappush

input = sys.stdin.readline

INF = float('inf')


def dijkstra(start):
    distances = [INF] * (N + 1)
    queue = [(0, start)]
    distances[start] = 0
    prev = [-1] * (N + 1)

    while queue:
        curr_distance, curr_node = heappop(queue)

        if distances[curr_node] != curr_distance:
            continue

        for next_node, weight in adj[curr_node].items():
            if (distance := curr_distance + weight) < distances[next_node]:
                distances[next_node] = distance
                heappush(queue, (distance, next_node))
                prev[next_node] = curr_node

    # print(distances)
    # print(prev)
    result_set = set()
    for i in range(2, N + 1):
        curr_node = i
        while curr_node != 1:
            next_node = prev[curr_node]
            result_set.add((curr_node, next_node))
            curr_node = next_node

    return result_set


N, M = map(int, input().split())

adj = defaultdict(dict)

for _ in range(M):
    V1, V2, W = map(int, input().split())
    adj[V1][V2] = W
    adj[V2][V1] = W

result = dijkstra(1)
print(len(result))
for r in result:
    print(*r)
