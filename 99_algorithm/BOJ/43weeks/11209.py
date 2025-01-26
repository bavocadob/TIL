import heapq
import sys

input = sys.stdin.readline
INF = float('inf')


def solve():
    dist = [INF] * N

    dist[s] = 0
    prev = [list() for _ in range(N)]

    queue = [(0, s)]

    while queue:
        d, curr = heapq.heappop(queue)

        for to, weight in adj[curr].items():

            if (temp := d + weight) < dist[to]:
                dist[to] = temp
                prev[to] = [(curr, weight)]
                heapq.heappush(queue, (temp, to))
            elif temp == dist[to]:
                prev[to].append((curr, weight))

    queue = [(0, t)]
    rst = []
    dist = [INF] * N
    dist[t] = 0
    while queue:
        d, curr = heapq.heappop(queue)

        if not queue:
            rst.append(curr)

        for to, weight in prev[curr]:
            if (temp := d + weight) < dist[to]:
                dist[to] = temp
                heapq.heappush(queue, (temp, to))

    print(*sorted(rst))


N, M = map(int, input().split())

adj = [dict() for _ in range(N)]

for _ in range(M):
    u, v, w = map(int, input().split())

    if v in adj[u]:
        adj[u][v] = min(adj[u][v], w)
    else:
        adj[u][v] = w

    if u in adj[v]:
        adj[v][u] = min(adj[v][u], w)
    else:
        adj[v][u] = w

s, t = map(int, input().split())
solve()
