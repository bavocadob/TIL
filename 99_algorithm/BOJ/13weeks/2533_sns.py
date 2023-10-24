import sys

sys.setrecursionlimit(999999)
input = sys.stdin.readline

INF = int(1e9)
N = int(input())
visited = [False] * (N + 1)


def solution(node):
    visited[node] = True
    dp[0][node] = 1

    for next_node in adj[node]:
        if not visited[next_node]:
            solution(next_node)
            dp[1][node] += dp[0][next_node]
            dp[0][node] += min(dp[0][next_node], dp[1][next_node])


adj = [list() for _ in range(N + 1)]

dp = [[0] * (N + 1) for _ in range(2)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

solution(1)

# print(dp)
print(min(dp[1][1], dp[0][1]))
