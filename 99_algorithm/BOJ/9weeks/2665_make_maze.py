import heapq
import sys

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
N = int(input())

INF = float('inf')


def dijkstra(start_x, start_y, end_x, end_y):
    visited = [[INF] * N for _ in range(N)]
    visited[start_x][start_y] = 0
    queue = [(0, start_x, start_y)]

    while queue:
        curr_dist, curr_x, curr_y = heapq.heappop(queue)
        if visited[curr_x][curr_y] != curr_dist:
            continue

        if curr_x == end_x and curr_y == end_y:
            return curr_dist

        for k in range(4):
            nx, ny = curr_x + dx[k], curr_y + dy[k]
            if 0 > nx or 0 > ny or N <= nx or N <= ny:
                continue
            dist = curr_dist
            if not maze[nx][ny]:
                dist += 1

            if dist < visited[nx][ny]:
                visited[nx][ny] = dist
                heapq.heappush(queue, (dist, nx, ny))

    # return visited[end_x][end_y]


maze = [list(map(int, input().rstrip())) for _ in range(N)]

print(dijkstra(0, 0, N - 1, N - 1))
