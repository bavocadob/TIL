import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M = map(int, input().split())

adj = [defaultdict(int) for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())

    adj[a][b] = max(adj[a][b], c)
    adj[b][a] = max(adj[b][a], c)

dp = [0] * (N + 1)
queue = deque()

start, end = map(int, input().split())
for next_node, w in adj[start].items():
    queue.append((next_node, w))

    dp[next_node] = w

while queue:
    curr, weight = queue.popleft()
    if weight < dp[curr]:
        continue

    for next_node, w in adj[curr].items():
        next_weight = min(weight, w)
        if next_weight > dp[next_node]:
            dp[next_node] = next_weight
            queue.append((next_node, next_weight))

print(dp[end])
