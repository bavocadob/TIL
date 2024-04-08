import sys

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

N = int(input())

dp = [0] * N
parents = [0] * N

adj = [list() for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    parents[b] += 1

value = list(map(int, input().split()))

root = -1
for i in range(N):
    if parents[i] == 0:
        root = i
        break


def solve(node):
    dp[node] = value[node]

    for child in adj[node]:
        solve(child)
        if dp[child] > 0:
            dp[node] += dp[child]


solve(root)

print(dp[root])
