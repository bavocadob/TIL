import heapq
import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

INF = float('inf')


def valid(x, y):
    return 0 <= x < N and 0 <= y < N and room[x][y] != '*'


def dijkstra():
    dp = [[[INF] * N for _ in range(N)] for _ in range(4)]
    queue = []

    for k in range(4):
        dp[k][doors[0][0]][doors[0][1]] = 0
        queue.append((0, k, doors[0][0], doors[0][1]))

    while queue:
        curr_dist, curr_dir, curr_x, cuur_y = heapq.heappop(queue)

        if dp[curr_dir][curr_x][cuur_y] < curr_dist:
            continue

        if curr_x == doors[1][0] and cuur_y == doors[1][1]:
            return curr_dist

        if room[curr_x][cuur_y] != '!':
            nx, ny = curr_x + dx[curr_dir], cuur_y + dy[curr_dir]
            if valid(nx, ny) and dp[curr_dir][nx][ny] > curr_dist:
                dp[curr_dir][nx][ny] = curr_dist
                heapq.heappush(queue, (curr_dist, curr_dir, nx, ny))
        else:
            for k in range(4):
                nx, ny = curr_x + dx[k], cuur_y + dy[k]
                if valid(nx, ny):
                    distance = curr_dist
                    if k != curr_dir:
                        distance += 1

                    if dp[k][nx][ny] > distance:
                        dp[k][nx][ny] = distance
                        heapq.heappush(queue, (distance, k, nx, ny))


N = int(input())

room = [list(input()) for _ in range(N)]

doors = []

for i in range(N):
    for j in range(N):
        if room[i][j] == '#':
            doors.append((i, j))

print(dijkstra())
