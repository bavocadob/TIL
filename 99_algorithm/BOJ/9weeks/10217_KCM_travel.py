from collections import defaultdict  # , deque
import heapq
import sys

input = sys.stdin.readline

INF = float('inf')


def dijkstra(start, end):
    # distances = defaultdict(dict)
    distances = [[INF for _ in range(M + 1)] for _ in range(N + 1)]
    distances[start][0] = 0

    # dp = [(INF, INF) for _ in range(N + 1)]
    # queue = deque([(0, 0, start)])
    queue = [(0, 0, start)]

    while queue:
        curr_dist, curr_cost, curr_node = heapq.heappop(queue)
        # curr_dist, curr_cost, curr_node = queue.popleft()
        if distances[curr_node][curr_cost] < curr_dist:
            continue
        # print(curr_dist,curr_node)

        if end == curr_node:
            return curr_dist
        # print(curr_node, curr_cost)
        # distances[curr_node][curr_cost] = curr_dist

        for next_node in adj[curr_node].keys():
            for next_cost, next_dist in adj[curr_node][next_node].items():
                if (cost := curr_cost + next_cost) > M:
                    continue
                if (distance := curr_dist + next_dist) < distances[next_node][cost]:
                    for i in range(cost, M + 1):
                        if distances[next_node][i] > distance:
                            distances[next_node][i] = distance
                        else:
                            break
                    heapq.heappush(queue, (distance, cost, next_node))

    return 'Poor KCM'


T = int(input())

for tc in range(T):
    N, M, K = map(int, input().split())

    adj = defaultdict(dict)

    for _ in range(K):
        u, v, c, d = map(int, input().split())
        adj_dict = adj[u].setdefault(v, dict())
        adj_dist = adj_dict.setdefault(c, INF)
        adj_dict[c] = min(adj_dist, d)

    print(dijkstra(1, N))
