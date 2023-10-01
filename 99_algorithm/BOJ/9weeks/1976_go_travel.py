import sys

from collections import defaultdict

input = sys.stdin.readline


def dfs(idx):
    for next_node in adj[idx]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node)


N = int(input())

M = int(input())

adj = defaultdict(list)

for i in range(1, N + 1):
    edges = list(map(int, input().split()))
    for j in range(N):
        if edges[j]:
            adj[i].append(j + 1)

visited = [False] * (N + 1)

journey = list(map(int, input().split()))
visited[journey[0]] = True
dfs(journey[0])

ans = True
for j in journey:
    if not visited[j]:
        ans = False
        break

if ans:
    print('YES')
else:
    print('NO')
