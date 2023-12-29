import heapq

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

INF = int(1e9)


def dijkstra():
    rst = [[INF] * 501 for _ in range(501)]
    rst[0][0] = 0

    queue = [(0, 0, 0)]

    while queue:
        dist, i, j = heapq.heappop(queue)

        if dist != rst[i][j]:
            continue

        for k in range(4):
            ni, nj = i + dx[k], j + dy[k]
            if 0 <= ni <= 500 and 0 <= nj <= 500:
                next_dist = road[ni][nj] + dist
                if next_dist < rst[ni][nj]:
                    rst[ni][nj] = next_dist
                    heapq.heappush(queue, (next_dist, ni, nj))

    if rst[500][500] != INF:
        return rst[500][500]
    else:
        return -1


road = [[0] * 501 for _ in range(501)]

N = int(input())

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            road[x][y] = 1

N = int(input())

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            road[x][y] = INF

print(dijkstra())
