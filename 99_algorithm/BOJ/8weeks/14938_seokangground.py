import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

INF = int(1e9)


def dijkstra(start, adj, N, M):
    queue = [(0, start)]
    distance = [INF] * (N + 1)
    distance[start] = 0

    while queue:
        value, node = heapq.heappop(queue)

        if value > distance[node]:
            continue

        for next_node, weight in adj[node].items():
            if (next_weight := weight + value) < distance[next_node] and next_weight <= M:
                distance[next_node] = next_weight
                heapq.heappush(queue, (next_weight, next_node))

    return distance


def solution():
    N, M, R = map(int, input().split())
    items = list(map(int, input().split()))

    adj = defaultdict(dict)

    for _ in range(R):
        a, b, l = map(int, input().split())
        adj[a][b] = l
        adj[b][a] = l

    ans = 0
    for i in range(1, N + 1):
        temp = 0
        distance = dijkstra(i, adj, N, M)
        for j in range(1, N + 1):
            if distance[j] != INF:
                temp += items[j - 1]

        ans = max(temp, ans)

    print(ans)


if __name__ == '__main__':
    solution()
