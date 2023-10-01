import heapq
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def dijkstra():
    distances = [[[INF] * M for _ in range(N)] for _ in range(4)]
    queue = []
    for k in range(4):
        distances[k][lasers[0][0]][lasers[0][1]] = 0
        heapq.heappush(queue, (0, k, lasers[0][0], lasers[0][1]))

    while queue:
        curr_dist, curr_dir, curr_x, curr_y = heapq.heappop(queue)

        if distances[curr_dir][curr_x][curr_y] > curr_dist:
            continue

        if curr_x == lasers[1][0] and curr_y == lasers[1][1]:
            return curr_dist

        for k in range(4):
            nx, ny = curr_x + dx[k], curr_y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and space[nx][ny] != '*':
                dist = curr_dist
                if distances[k][nx][ny] > dist:
                    if k != curr_dir:
                        dist += 1
                    distances[k][nx][ny] = dist
                    heapq.heappush(queue, (dist, k, nx, ny))


M, N = map(int, input().split())
INF = int(1e9)
space = [list(input().rstrip()) for _ in range(N)]

lasers = []

for i in range(N):
    for j in range(M):
        if space[i][j] == 'C':
            lasers.append((i, j))

print(dijkstra())
