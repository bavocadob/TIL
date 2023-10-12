import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

adj = [list() for _ in range(N + 1)]

parent = [0] * (N + 1)

for _ in range(M):
    v, e = map(int, input().split())
    adj[v].append(e)
    parent[e] += 1

queue = deque()
for i in range(1, N + 1):
    if not parent[i]:
        queue.append(i)

result = []
while queue:
    v = queue.popleft()
    result.append(v)
    for e in adj[v]:
        parent[e] -= 1
        if not parent[e]:
            queue.append(e)

print(*result)
