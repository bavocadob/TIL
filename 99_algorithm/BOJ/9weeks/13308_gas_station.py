import sys

from collections import defaultdict
from heapq import heappop, heappush

input = sys.stdin.readline

INF = float('inf')


def dijkstra(start, end):
    # distances = [(INF, INF)] * (N + 1)
    distances = defaultdict(dict)
    distances[start][cost[start]] = 0
    queue = [(0, cost[start], start)]

    while queue:
        curr_cost, min_price, curr_node = heappop(queue)

        if distances[curr_node][min_price] < curr_cost:
            continue

        if curr_node == end:
            return curr_cost

        for next_node, weight in adj[curr_node].items():
            price = min(min_price, cost[curr_node])
            distance = curr_cost + (price * weight)
            if distances[next_node].setdefault(price, INF) > distance:
                distances[next_node][price] = distance
                heappush(queue, (distance, price, next_node))

    # print(distances)
    # min_cost = min(distances[end].values())
    # return min_cost


N, M = map(int, input().split())

cost = [INF] + list(map(int, input().split()))

adj = defaultdict(dict)

for _ in range(M):
    a, b, l = map(int, input().split())
    adj[a][b] = l
    adj[b][a] = l

ans = dijkstra(1, N)
print(ans)
