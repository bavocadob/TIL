import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline
INF = float('inf')


def dijkstra(start, end):
    distances = [INF] * N
    queue = [(0, start)]
    while queue:
        curr_dist, curr_node = heapq.heappop(queue)
        if distances[curr_node] < curr_dist:
            continue

        if curr_node == end:
            return curr_dist

        for next_node, weight in adj[curr_node].items():
            if not ward[next_node] and distances[next_node] > (distance := curr_dist + weight):
                distances[next_node] = distance
                heapq.heappush(queue, (distance, next_node))

    return -1


N, M = map(int, input().split())

ward = list(map(int, input().split()))
ward[N - 1] = 0
adj = defaultdict(dict)

for _ in range(M):
    v, e, p = map(int, input().split())
    adj[v][e] = p
    adj[e][v] = p

print(dijkstra(0, N - 1))
