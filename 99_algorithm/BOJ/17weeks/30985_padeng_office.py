import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)


def dijkstra():
    ans = 0

    distance = [[INF] * (N + 1) for _ in range(2)]
    # 0은 1층 / 1은 K층

    distance[0][1] = 0

    queue = [(0, 0, 1)]

    while queue:
        dist, floor, node = heapq.heappop(queue)

        if distance[floor][node] != dist:
            continue

        for cost, next_node in adj[node]:
            new_dist = dist + cost

            if new_dist < distance[floor][next_node]:
                distance[floor][next_node] = new_dist
                heapq.heappush(queue, (new_dist, floor, next_node))

        if floor == 0 and E[node] != -1:
            new_dist = dist + (E[node] * (K - 1))
            if new_dist < distance[1][node]:
                distance[1][node] = new_dist
                heapq.heappush(queue, (new_dist, 1, node))

    if distance[1][N] != INF:
        return distance[1][N]
    else:
        return -1


N, M, K = map(int, input().split())

adj = [list() for _ in range(N + 1)]

for _ in range(M):
    u, v, c = map(int, input().split())
    adj[u].append((c, v))
    adj[v].append((c, u))

E = [0] + list(map(int, input().split()))

print(dijkstra())
