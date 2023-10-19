import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

time = [0] * N

parents = [0] * N

adj = [list() for _ in range(N)]

for i in range(N):
    cost, *nodes, _ = map(int, input().split())

    time[i] = cost
    parents[i] = len(nodes)
    for node in nodes:
        adj[node - 1].append(i)

result = [0] * N

queue = deque()

for i, v in enumerate(parents):
    if not v:
        queue.append(i)
        result[i] = time[i]

while queue:
    curr_node = queue.popleft()
    for next_node in adj[curr_node]:
        parents[next_node] -= 1
        result[next_node] = max(result[curr_node] + time[next_node], result[next_node])
        if not parents[next_node]:
            queue.append(next_node)

for t in result:
    print(t)
