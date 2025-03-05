import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
adj = [[] for _ in range(N + 1)]
dp = [0] * (N + 1)
visited = [False] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)


def dfs(node):
    visited[node] = True
    dp[node] = 1
    for child in adj[node]:
        if not visited[child]:
            dp[node] += dfs(child)
    return dp[node]


dfs(1)

ans = 0

visited = [False] * (N + 1)


def dfs2(node):
    global ans
    visited[node] = True
    ans = max(ans, (N - dp[node]) * dp[node])
    for child in adj[node]:
        if not visited[child]:
            dfs2(child)


dfs2(1)
print(ans)
