import sys
input = sys.stdin.readline

def dfs(depth, node):
    global result
    if depth == 4 or result:
        result = True
        return

    for c in connection[node]:
        if not visited[c]:
            visited[c] = True
            dfs(depth + 1, c)
            visited[c] = False


N, M = map(int, input().split())

visited = [False] * N

connection = [list() for _ in range(N)]

for _ in range(M):
    x, y = map(int, input().split())
    connection[x].append(y)
    connection[y].append(x)

result = False


for i in range(N):
    visited[i] = True
    dfs(0, i)
    visited[i] = False

print(int(result))