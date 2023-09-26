import sys
from heapq import heappop, heappush

# sys.stdin = open('input.txt')
input = sys.stdin.readline
INF = float('inf')


def dijkstra(start_x, start_y, end_x, end_y):
    distances = [[[INF] * 2 for _ in range(len(adj[i]))] for i in range(N + 1)]
    # print(distances)
    distances[start_x][start_y][0] = 0
    queue = [(0, start_x, start_y, 0)]

    while queue:
        curr_time, curr_line, curr_station, on_subway = heappop(queue)
        if distances[curr_line][curr_station][on_subway] != curr_time:
            continue

        for next_line, next_station, weight in adj[curr_line][curr_station]:
            distance = curr_time + weight
            if curr_line != next_line:
                if distances[next_line][next_station][0] > distance:
                    distances[next_line][next_station][0] = distance
                    heappush(queue, (distance, next_line, next_station, 0))
            else:
                if on_subway:
                    if distances[next_line][next_station][1] > distance:
                        distances[next_line][next_station][1] = distance
                        heappush(queue, (distance, next_line, next_station, 1))
                else:
                    if distances[next_line][next_station][1] > distance + waiting_time[curr_line]:
                        distances[next_line][next_station][1] = distance + waiting_time[curr_line]
                        heappush(queue, (distance + waiting_time[curr_line], next_line, next_station, 1))

    # print(distances)
    # print()
    return min(distances[end_x][end_y][0], distances[end_x][end_y][1])


tc = int(input())

for ttc in range(tc):
    input()
    N = int(input())  # 노선 갯수

    adj = [list() for _ in range(N + 1)]  # 그래프

    waiting_time = [0] * (N + 1)  # 각 노선별 대기해야하는 시간
    for i in range(1, N + 1):
        M, W = map(int, input().split())
        adj[i] = [list() for _ in range(M + 1)]
        waiting_time[i] = W
        costs = list(map(int, input().split()))
        for j in range(1, M):
            adj[i][j].append((i, j + 1, costs[j - 1]))
            adj[i][j + 1].append((i, j, costs[j - 1]))

    T = int(input())  # 환승역 개수

    for _ in range(T):
        x1, y1, x2, y2, W2 = map(int, input().split())
        adj[x1][y1].append((x2, y2, W2))
        adj[x2][y2].append((x1, y1, W2))

    # for a input.txt adj:
    #     print(a)
    Q = int(input())

    print(f'Case #{ttc + 1}:')
    for _ in range(Q):
        x1, y1, x2, y2 = map(int, input().split())
        min_time = dijkstra(x1, y1, x2, y2)
        if min_time != INF:
            print(min_time)
        else:
            print(-1)
