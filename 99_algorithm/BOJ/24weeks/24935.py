import sys

sys.setrecursionlimit(9999)
input = sys.stdin.readline


def dfs(node, weight):
    global ans

    is_need = False

    if node in target:
        is_need = True

    for next_node, ww in adj[node]:
        is_need = is_need | dfs(next_node, ww)

    if is_need:
        ans += weight

    return is_need


N, K = map(int, input().split())

adj = [list() for _ in range(N)]

for _ in range(N - 1):
    s, e, w = map(int, input().split())
    adj[s].append((e, w))

target = set(map(int, input().split()))
ans = 0

dfs(0, 0)
print(ans * 2)
