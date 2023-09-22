import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start, end, adj_list):
    distance = [INF] * (N + 1)
    hq = [(0, start)]
    prev = [-1] * (N + 1)
    while hq:
        value, node = heapq.heappop(hq)

        if distance[node] < value:
            continue

        for weight, next_node in adj_list[node]:
            if (new_weight := weight + value) < distance[next_node]:
                prev[next_node] = node
                distance[next_node] = new_weight
                heapq.heappush(hq, (new_weight, next_node))

    return distance[end], prev


N = int(input())
M = int(input())
adj = defaultdict(list)

for _ in range(M):
    s, e, w = map(int, input().split())
    adj[s].append((w, e))

left, right = map(int, input().split())
ans, p = dijkstra(left, right, adj)
prevs = [right]
while right != left:
    prevs.append(p[right])
    right = p[right]

print(ans)
print(len(prevs))
print(*prevs[::-1])

