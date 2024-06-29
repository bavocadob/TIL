import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)


def dijkstra():
    distances = [INF] * (N + 1)
    distances[1] = 0

    Q = [(0, 1, 0)]

    while Q:
        dist, node, cnt = heapq.heappop(Q)

        if distances[node] != dist:
            continue

        for next_node, cost, gap in adj[node]:
            mod = (gap - dist) % gap
            if mod and cnt < K:
                if distances[next_node] > dist + cost:
                    distances[next_node] = dist + cost
                    heapq.heappush(Q, (dist + cost, next_node, cnt + 1))

            if distances[next_node] > dist + cost + mod:
                distances[next_node] = dist + cost + mod
                heapq.heappush(Q, (dist + cost + mod, next_node, cnt))

    if distances[N] != INF:
        return distances[N]
    else:
        return -1


N, M, K = map(int, input().split())

adj = [list() for _ in range(N + 1)]

for _ in range(M):
    s, e, t, g = map(int, input().split())
    adj[s].append((e, t, g))

print(dijkstra())
