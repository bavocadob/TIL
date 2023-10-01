import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline

INF = float('inf')


def dijkstra(start, end):
    queue = [(0, 0, start)]
    distances = [[INF] * (N + 1) for _ in range(K + 1)]  # distances[i][j]는 i번 공사해서 j번 노드까지 갈 수 있는 최단거리
    distances[0][start] = 0

    while queue:
        curr_dist, curr_cnt, curr_node = heapq.heappop(queue)
        if distances[curr_cnt][curr_node] < curr_dist:
            continue

        if curr_node == end:
            return curr_dist

        for next_node, weight in adj[curr_node].items():
            distance = curr_dist + weight
            if distances[curr_cnt][next_node] > distance:
                distances[curr_cnt][next_node] = distance
                heapq.heappush(queue, (distance, curr_cnt, next_node))

            if curr_cnt < K:
                if distances[curr_cnt + 1][next_node] > curr_dist:
                    distances[curr_cnt + 1][next_node] = curr_dist
                    heapq.heappush(queue, (curr_dist, curr_cnt + 1, next_node))

    return distances[K][end]


N, M, K = map(int, input().split())

adj = defaultdict(dict)

for _ in range(M):
    e, v, p = map(int, input().split())

    adj[e][v] = min(p, adj[e].setdefault(v, INF))
    adj[v][e] = min(p, adj[v].setdefault(e, INF))

print(dijkstra(1, N))
