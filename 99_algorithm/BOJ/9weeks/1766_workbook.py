import heapq
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

adj = [list() for _ in range(N + 1)]
parent = [0] * (N + 1)
for _ in range(M):
    v, e = map(int, input().split())
    adj[v].append(e)
    parent[e] += 1

queue = []
result = []
for i in range(1, N + 1):
    if not parent[i]:
        heapq.heappush(queue, i)

while queue:
    quiz = heapq.heappop(queue)
    result.append(quiz)

    for v in adj[quiz]:
        parent[v] -= 1
        if not parent[v]:
            heapq.heappush(queue, v)

print(*result)
