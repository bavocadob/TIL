import heapq
import sys

sys.setrecursionlimit(999999)

def dfs(node, tree, depth, parent, start):
    is_leaf = True

    for next_node in tree[node]:
        if next_node != parent:
            dfs(next_node, tree, depth + 1, node, start)
            is_leaf = False

    if is_leaf:
        heapq.heappush(candidate, depth + start)


N = int(input())

candidate = [0]

for _ in range(N):
    start_depth = heapq.heappop(candidate)
    size = int(input())
    adj = [list() for _ in range(size + 1)]

    for _ in range(size - 1):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    dfs(1, adj, 1, -1, start_depth)

ans = max(candidate)
print(ans)
