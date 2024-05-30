import sys
from collections import deque

input = sys.stdin.readline

P, C, N = map(int, input().split())

# P개의 목초지, C개의 간선, N개의 멀쩡한 목초지


adj = [list() for _ in range(P + 1)]

for _ in range(C):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [False] * (P + 1)

for _ in range(N):
    a = int(input())
    for neighbor in adj[a]:
        visited[neighbor] = True

queue = deque([1])

ans = P - 1
visited[1] = True
while queue:
    node = queue.popleft()

    for next_node in adj[node]:
        if visited[next_node]:
            continue

        visited[next_node] = True
        ans -= 1
        queue.append(next_node)

print(ans)
