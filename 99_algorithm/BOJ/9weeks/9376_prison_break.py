import heapq
import sys

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

INF = float('inf')


def valid(x, y):
    return 0 <= x < H + 2 and 0 <= y < W + 2


def bfs(start_x, start_y):
    queue = [(0, start_x, start_y)]
    visited = [[INF] * (W + 2) for _ in range(H + 2)]
    visited[start_x][start_y] = 0
    while queue:
        curr_distance, x, y = heapq.heappop(queue)
        if curr_distance > visited[x][y]:
            continue

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if valid(nx, ny) and visited[nx][ny] == INF:
                # print(nx, ny)
                if jail[nx][ny] >= 0:
                    visited[nx][ny] = visited[x][y] + jail[nx][ny]
                    heapq.heappush(queue, (visited[nx][ny], nx, ny))

    return visited


T = int(input())

for tc in range(T):
    H, W = map(int, input().split())

    jail = [[0] * (W + 2)]

    prisoner = []
    for i in range(H):
        jail_line = [0]
        jail_input = input()
        for j in range(W):
            if jail_input[j] == '*':
                jail_line.append(-1)
            elif jail_input[j] == '#':
                jail_line.append(1)
            else:
                jail_line.append(0)
                if jail_input[j] == '$':
                    prisoner.append((i + 1, j + 1))
        jail_line.append(0)
        jail.append(jail_line)
    jail.append([0] * (W + 2))

    # for j input.txt jail:
    #     print(j)

    distance_prisoner_1 = bfs(*prisoner[0])
    distance_prisoner_2 = bfs(*prisoner[1])
    distance_outside = bfs(0, 0)

    result = INF
    for i in range(H + 2):
        for j in range(W + 2):
            temp_distance = distance_outside[i][j] + distance_prisoner_1[i][j] + distance_prisoner_2[i][j]
            if jail[i][j] == 1:
                temp_distance -= 2
            result = min(temp_distance, result)

    print(result)
