import heapq
import sys

input = sys.stdin.readline

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

INF = int(1e9)


def solve():
    distances = [[INF] * M for _ in range(N)]

    distances[0][0] = 0

    queue = [(0, 0, 0)]
    while queue:
        dist, x, y = heapq.heappop(queue)

        if dist > distances[x][y]:
            continue

        if (x, y) == (N - 1, M - 1):
            break

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < N and 0 <= ny < M:
                next_dist = dist + maze[nx][ny]
                if next_dist < distances[nx][ny]:
                    distances[nx][ny] = next_dist
                    heapq.heappush(queue, (next_dist, nx, ny))

    return distances[N - 1][M - 1]


M, N = map(int, input().split())

maze = []

for i in range(N):
    temp = input().rstrip()
    maze.append(list())
    for j in range(M):
        maze[i].append(int(temp[j]))

print(solve())
