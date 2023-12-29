import heapq
import sys

input = sys.stdin.readline


def eratosthenes_sieve(n):
    is_prime = [False, False] + [True] * (n - 1)
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime


def dijkstra():
    distances = [INF] * (N + 1)
    distances[1] = 0
    queue = [(0, 1)]

    while queue:
        dist, node = heapq.heappop(queue)

        if dist != distances[node]:
            continue

        if node == N:
            return dist

        for next_node, weight in adj[node].items():
            next_dist = dist + weight
            if next_dist < distances[next_node]:
                distances[next_node] = next_dist
                heapq.heappush(queue, (next_dist, next_node))

    return 'Now where are you?'


prime = eratosthenes_sieve(10_000_000)

INF = float('inf')

N, M = map(int, input().split())

code = [0] + list(map(int, input().split()))

adj = [dict() for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())

    if not prime[code[u] + code[v]]:
        continue

    temp = adj[u].get(v, INF)
    if temp > w:
        adj[u][v] = w
        adj[v][u] = w

print(dijkstra())
