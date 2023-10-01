import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start, end):
    distances = [INF] * (V + 1)
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        curr_dist, curr_node = heapq.heappop(queue)
        if distances[curr_node] < curr_dist:
            continue

        for next_node, weight in adj[curr_node].items():
            if distances[next_node] > (distance := curr_dist + weight):
                distances[next_node] = distance
                heapq.heappush(queue, (distance, next_node))

    return distances


V, E, P = map(int, input().split())

adj = defaultdict(dict)
for _ in range(E):
    a, b, c = map(int, input().split())
    adj[a][b] = c
    adj[b][a] = c

a_to_b = dijkstra(1, V)
b_to_a = dijkstra(V, 1)
# print(a_to_b)
# print(b_to_a)

if a_to_b[V] == a_to_b[P] + b_to_a[P]:
    print('SAVE HIM')
else:
    print('GOOD BYE')
