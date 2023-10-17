import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N = int(input())


def dfs(node):
    visited[node] = True
    if in_out[node]:
        return 1

    cnt = 0
    for next_node in adj[node]:
        if visited[next_node]:
            continue
        if in_out[next_node]:
            cnt += 1
        else:
            cnt += dfs(next_node)

    return cnt


# 1은 실내 0은 실외
# 1로 시작해서 1로 끝나는 사이가 0인 트리 경로 계산
in_out = [0] + list(map(int, list(input().rstrip())))

adj = [list() for _ in range(N + 1)]

ans = 0

for _ in range(N - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
    if in_out[u] and in_out[v]:
        ans += 2

visited = [False] * (N + 1)

for i in range(1, N + 1):
    if not visited[i] and in_out[i] == 0:
        c = dfs(i)
        ans += c * (c - 1)

print(ans)
