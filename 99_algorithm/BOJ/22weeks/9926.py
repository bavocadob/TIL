import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)
N = int(input())

cost = [list(map(int, input().split())) for _ in range(N)]

dp = [[[INF] * 4 for _ in range(N)] for _ in range(N)]

# 0 1 2 3
# 상하좌우

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = []
for k in range(4):
    dp[0][0][k] = 0
    queue.append((0, 0, 0, k))

while queue:
    dist, x, y, d = heapq.heappop(queue)

    if dp[x][y][d] != dist:
        continue

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]

        if not (0 <= nx < N and 0 <= ny < N):
            continue

        c = cost[nx][ny]
        if k != d:
            c += 3

        if dist + c < dp[nx][ny][k]:
            dp[nx][ny][k] = dist + c
            heapq.heappush(queue, (dist + c, nx, ny, k))

ans = INF
for k in range(4):
    ans = min(ans, dp[N - 1][N - 1][k])

print(ans)

