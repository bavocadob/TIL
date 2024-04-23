from collections import deque

INF = int(1e9)

N, M = map(int, input().split())
adj = [[-1 for _ in range(N)] for _ in range(N)]
dp = [[INF for _ in range(N)] for _ in range(N)]
queue = deque()

for _ in range(M):
    a, b, c = input().split()
    a, b = int(a), int(b)
    adj[a][b] = adj[b][a] = ord(c) - ord('a')
    dp[a][b] = dp[b][a] = 1
    queue.append((a, b))

for i in range(N):
    for j in range(i + 1, N):
        for k in range(N):
            if k == i or k == j or adj[i][k] == -1 or adj[k][j] == -1:
                continue
            if adj[i][k] == adj[k][j] and dp[i][j] == INF:
                dp[i][j] = dp[j][i] = 2
                queue.append((i, j))

while queue:
    a, b = queue.popleft()
    for i in range(N):
        if i == a or i == b:
            continue
        for j in range(N):
            if j == i or j == a or j == b:
                continue
            if adj[a][i] == -1 or adj[b][j] == -1:
                continue
            if adj[a][i] == adj[b][j] and dp[i][j] > dp[a][b] + 2:
                dp[i][j] = dp[j][i] = dp[a][b] + 2
                queue.append((i, j))

if dp[0][1] == INF:
    print(-1)
else:
    print(dp[0][1])
