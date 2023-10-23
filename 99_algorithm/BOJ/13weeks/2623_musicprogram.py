import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

parents = [0] * (N + 1)
adj = [list() for _ in range(N + 1)]

for _ in range(M):
    c, *musicians = map(int, input().split())

    for i in range(1, c):
        adj[musicians[i - 1]].append(musicians[i])
        parents[musicians[i]] += 1

result = []
queue = deque()
for i in range(1, N + 1):
    if not parents[i]:
        queue.append(i)

while queue:
    now = queue.popleft()
    result.append(now)

    for next_node in adj[now]:
        parents[next_node] -= 1
        if not parents[next_node]:
            queue.append(next_node)

if len(result) == N:
    for r in result:
        print(r)
else:
    print(0)
