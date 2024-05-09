import heapq
import sys

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dijkstra(hq, dist):
    while hq:
        d, x, y = heapq.heappop(hq)

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if dist[nx][ny] == -1:
                dist[nx][ny] = d + 1 + L
                heapq.heappush(hq, (dist[nx][ny], nx, ny))
            elif dist[nx][ny] == INF:
                dist[nx][ny] = d + 1
                heapq.heappush(hq, (dist[nx][ny], nx, ny))


INF = int(1e9)
N, M = map(int, input().split())

K, L, X, B = map(int, input().split())

queue = []

distances = [[INF] * M for _ in range(N)]
for i in range(N):
    line = input().rstrip()
    for j in range(M):
        if line[j] == '*':
            distances[i][j] = 0
            queue.append((0, i, j))
        elif line[j] == '#':
            distances[i][j] = -1

dijkstra(queue, distances)
ans = 0
for i in range(N):
    for j in range(M):
        if distances[i][j] > K or distances[i][j] == -1:
            print(i + 1, j + 1)
            ans += 1

if not ans:
    print(-1)
