import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline
INF = float('inf')


def fox_dijkstra(start):
    distances = [INF] * (N + 1)
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        curr_dist, curr_node = heapq.heappop(queue)

        if curr_dist > distances[curr_node]:
            continue

        for next_node, weight in adj[curr_node].items():
            if (distance := curr_dist + weight) < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(queue, (distance, next_node))
    return distances


def wolf_dijkstra(start):
    distances = [[INF] * (N + 1) for _ in range(2)]
    distances[0][start] = 0
    queue = [(0, start, 0)]

    while queue:
        curr_dist, curr_node, need_rest = heapq.heappop(queue)

        if curr_dist > distances[need_rest][curr_node]:
            continue

        for next_node, weight in adj[curr_node].items():
            temp_weight = weight
            temp_rest = not need_rest
            if need_rest:
                temp_weight *= 2
            else:
                temp_weight /= 2

            distance = temp_weight + curr_dist

            if distance < distances[temp_rest][next_node]:
                distances[temp_rest][next_node] = distance
                heapq.heappush(queue, (distance, next_node, temp_rest))
    return distances


N, M = map(int, input().split())
adj = defaultdict(dict)

for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a][b] = float(c)
    adj[b][a] = float(c)

fox_distance = fox_dijkstra(1)
wolf_distance = wolf_dijkstra(1)

cnt = 0
for i in range(2, N + 1):
    if fox_distance[i] < min(wolf_distance[0][i], wolf_distance[1][i]):
        cnt += 1

print(cnt)
