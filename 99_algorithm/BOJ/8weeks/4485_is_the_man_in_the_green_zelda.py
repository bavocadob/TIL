import sys
import heapq

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
INF = int(1e9)


def valid(x, y, n):
    return 0 <= x < n and 0 <= y < n


def dijkstra(cave, n):
    distance = [[INF] * (n + 1) for _ in range(n + 1)]
    distance[0][0] = 0
    queue = [(distance[0][0], 0, 0)]

    while queue:
        w, x, y = heapq.heappop(queue)
        if distance[x][y] < w:
            continue

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if valid(nx, ny, n):
                if (next_w := w + cave[x][y]) < distance[nx][ny]:
                    distance[nx][ny] = next_w
                    heapq.heappush(queue, (next_w, nx, ny))

    return distance


def solution(cnt, n):
    cave = [list(map(int, input().split())) for _ in range(n)]
    distance = dijkstra(cave, n)
    print(f'Problem {cnt}: {distance[n - 1][n - 1] + cave[n - 1][n - 1]}')


if __name__ == '__main__':
    c = 1
    while True:
        size = int(input())
        if size == 0:
            break
        solution(c, size)
        c += 1
