import heapq
import sys

input = sys.stdin.readline

INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def solve():
    distances = [[INF] * N for _ in range(N)]
    distances[0][0] = 0

    queue = [(0, 0, 0)]
    while queue:
        dist, x, y = heapq.heappop(queue)

        if distances[x][y] != dist:
            continue

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if not (0 <= nx < N and 0 <= ny < N):
                continue

            next_dist = max(dist, abs(A[x][y] - A[nx][ny]))

            if next_dist < distances[nx][ny]:
                distances[nx][ny] = next_dist
                heapq.heappush(queue, (next_dist, nx, ny))

    return distances[N - 1][N - 1]


N = int(input())

A = [list(map(int, input().split())) for _ in range(N)]

print(solve())
