import heapq
import sys

input = sys.stdin.readline


def solve():
    queue = [(0, 0)]

    distances = [INF] * N
    distances[0] = 0

    while queue:
        dist, node = heapq.heappop(queue)

        p_type = adj[node][0]

        if p_type == -1:
            next_dist = dist + 1

            if node + 1 < N and distances[node + 1] > next_dist:
                distances[node + 1] = next_dist
                heapq.heappush(queue, (next_dist, node + 1))
        elif p_type == 0:
            next_node = adj[node][1]

            if distances[next_node] > dist:
                distances[next_node] = dist
                heapq.heappush(queue, (dist, next_node))
        elif p_type == 1:
            next_node = adj[node][1]

            if distances[next_node] > dist:
                distances[next_node] = dist
                heapq.heappush(queue, (dist, next_node))

            next_dist = dist + 1

            if node + 1 < N and distances[node + 1] > next_dist:
                distances[node + 1] = next_dist
                heapq.heappush(queue, (next_dist, node + 1))

    if distances[N - 1] == INF:
        return -1
    else:
        return distances[N - 1]


INF = int(1e9)
N, C = map(int, input().split())

adj = [(-1, -1) for _ in range(N)]

# 0은 레드 1은 블루
for _ in range(C):
    t, a, b = map(int, input().split())

    adj[a] = (t, b)

print(solve())
