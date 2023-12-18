import sys

sys.setrecursionlimit(400000)
input = sys.stdin.readline


def dfs(node, depth, par):
    prev[node] = (par, depth)

    for next_node in adj[node]:
        if prev[next_node] == 0:
            dfs(next_node, depth + 1, node)


N, S, E = map(int, input().split())

adj = [list() for _ in range(N + 1)]

prev = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

dfs(S, 0, 0)

curr = prev[E][0]

first = True

# 후공은 방해, 선공은 직진
# depth가 짝수인 경우가 선공, 홀수인 경우가 후공의 턴
while curr:
    if prev[curr][1] % 2:
        if len(adj[curr]) > 2:
            first = False
            break

    curr = prev[curr][0]

print('First' if first else 'Second')
