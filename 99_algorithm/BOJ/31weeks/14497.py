import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def solve():
    distances = [[INF] * M for _ in range(N)]
    distances[x1][y1] = 0
    queue = [(0, x1, y1)]

    while queue:
        dist, x, y = heapq.heappop(queue)

        if distances[x][y] != dist:
            continue

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < N and 0 <= ny < M:
                next_dist = int(field[nx][ny]) + dist
                if next_dist >= distances[nx][ny]:
                    continue

                distances[nx][ny] = next_dist
                heapq.heappush(queue, (next_dist, nx, ny))

    return distances[x2][y2]


N, M = map(int, input().split())

x1, y1, x2, y2 = map(lambda x: int(x) - 1, input().split())

field = [list(input().rstrip()) for _ in range(N)]

field[x1][y1] = '0'
field[x2][y2] = '1'

print(solve())
