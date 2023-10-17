import sys

sys.setrecursionlimit(int(1e6))

input = sys.stdin.readline


def solution(node):
    cnt = 0

    for next_node in adj[node]:
        cnt += solution(next_node)
    dp[node] = max(0, cnt + motivations[node])
    return dp[node]


N = int(input())

adj = [list() for _ in range(N + 1)]

dp = [0] * (N + 1)
motivations = [0] * (N + 1)

for i in range(1, N + 1):
    parent, motivation = map(int, input().split())
    motivations[i] = motivation
    adj[parent].append(i)
solution(0)
result = max(dp)

if not result:
    result = max(motivations[1:])

print(result)
