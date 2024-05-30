import sys
from collections import deque

INF = int(1e9)
input = sys.stdin.readline


def dijkstra():
    start = 0
    end = 1

    queue = deque([(0, 0, 0)])  # 거리 비용 노드

    distances = [[INF] * N for _ in range(N)]
    distances[0][0] = 0

    while queue:
        dist, cost, node = queue.popleft()

        if node == 1:
            break

        if distances[node][dist] > cost:
            continue
        for next_node, val in adj[node]:
            if distances[next_node][dist + 1] > cost + val:
                distances[next_node][dist + 1] = cost + val
                queue.append((dist + 1, val, next_node))

    for val in distances[1]:
        if val != INF:
            return val


N, M = map(int, input().split())

adj = [list() for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))

print(dijkstra())
