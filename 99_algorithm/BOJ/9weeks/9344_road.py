import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline

INF = float('inf')


def mst(start, end):
    visited = [0] * (N + 1)
    visited[start] = start

    queue = []

    for next_node, weight in adj[start].items():
        heapq.heappush(queue, (weight, next_node, start))

    while queue:
        w, curr_node, parent_node = heapq.heappop(queue)

        visited[curr_node] = parent_node

        if curr_node == end:
            return visited[curr_node] == start

        for next_node, weight in adj[curr_node].items():
            if not visited[next_node]:
                heapq.heappush(queue, (weight, next_node, curr_node))


T = int(input())

for tc in range(T):
    N, M, p, q = map(int, input().split())

    adj = defaultdict(dict)

    for _ in range(M):
        u, v, w = map(int, input().split())
        adj[u][v] = w
        adj[v][u] = w

    if mst(p, q):
        print('YES')
    else:
        print('NO')
