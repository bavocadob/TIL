import heapq
import sys

input = sys.stdin.readline
INF = float('inf')


def dijkstra(start):
    distance = [INF] * (N + 1)
    distance[start] = 0

    heap = [(0, start)]

    while heap:
        curr_dist, curr_node = heapq.heappop(heap)

        if curr_dist > distance[curr_node]:
            continue

        for weight, next_node in adj[curr_node]:
            next_dist = curr_dist + weight
            if next_dist > distance[next_node]:
                continue

            distance[next_node] = next_dist
            heapq.heappush(heap, (next_dist, next_node))

    return distance


N, M, A, B = map(int, input().split())

adj = [list() for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    adj[u].append((w, v))
    adj[v].append((w, u))

dist_A = dijkstra(A)
dist_B = dijkstra(B)

rst = []

for i in range(1, N + 1):
    if dist_A[i] + dist_B[i] == dist_A[B]:
        rst.append(i)

print(len(rst))
print(*rst)
