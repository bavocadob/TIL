import sys

input = sys.stdin.readline
sys.setrecursionlimit(999999)

def dfs(idx):
    global cnt, cycle

    for node in adj[idx]:
        if not visited[node]:
            visited[node] = True
            cnt += 1
            dfs(node)
        elif node == betrayer:
            cycle += 1


N, M = map(int, input().split())

adj = [list() for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [False] * (N + 1)
betrayer = int(input())

ans = 0
visited[betrayer] = True
for next_node in adj[betrayer]:
    if not visited[next_node]:
        visited[next_node] = 1
        cnt = 2
        cycle = -1
        dfs(next_node)
        if cycle:
            cnt -= 1

        ans = max(ans, cnt)

for i in range(1, N + 1):
    if not visited[i]:
        visited[i] = True
        cnt = 1
        dfs(i)
        ans = max(ans, cnt)

print(ans)
