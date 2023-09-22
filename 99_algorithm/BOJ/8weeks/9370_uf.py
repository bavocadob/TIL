# import heapq
import sys
from collections import deque
from collections import defaultdict

input = sys.stdin.readline

INF = int(1e9)


# 나는 알고리즘을 못해요 # 나는 알고리즘을 못해요# 나는 알고리즘을 못해요# 나는 알고리즘을 못해요# 나는 알고리즘을 못해요# 나는 알고리즘을 못해요# 나는 알고리즘을 못해요


def dijkstra(N, start, adj):
    # prev = [-1] * (N + 1)
    distance = [INF] * (N + 1)
    distance[start] = 0
    # hq = [(0, start)]
    queue = deque([(0, start)])

    while queue:
        # value, node = heapq.heappop(hq)
        value, node = queue.popleft()
        if distance[node] < value:
            continue

        for next_node, weight in adj[node].items():
            if distance[next_node] > (next_weight := value + weight):
                # prev[next_node] = node
                distance[next_node] = next_weight
                # heapq.heappush(hq, (next_weight, next_node))
                queue.append((next_weight, next_node))
    return distance


def solution():
    N, M, T = map(int, input().split())

    S, G, H = map(int, input().split())

    adj = defaultdict(dict)

    for _ in range(M):
        a, b, d = map(int, input().split())
        adj[a][b] = d
        adj[b][a] = d

    # distance, prev = dijkstra(N, S, adj)
    distance = dijkstra(N, S, adj)
    if distance[H] > distance[G]:
        G = H

    distance_g = dijkstra(N, G, adj)

    result = []

    for _ in range(T):
        candidate = int(input())
        if distance[candidate] == INF:
            continue

        if distance_g[candidate] + distance[G] == distance[candidate]:
            result.append(candidate)

    # print(distance)
    # print(prev)
    print(*sorted(result))


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        solution()
