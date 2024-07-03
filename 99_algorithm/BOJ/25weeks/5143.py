import heapq
import sys

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

input = sys.stdin.readline

T = int(input())

for i in range(T):
    M, N = map(int, input().split())

    sea = []
    g = [[4] * M for _ in range(N)]

    start = None
    herring = []

    for j in range(N):
        temp = input().rstrip()
        sea.append(list(temp))
        for k in range(M):
            if sea[j][k] == 'S':
                start = (k, j)
            elif sea[j][k] == 'H':
                herring.append((k, j))

    queue = []
    heapq.heappush(queue, start)
    g[start[1]][start[0]] = 0

    while queue:
        u = heapq.heappop(queue)
        for j in range(4):
            v = (u[0] + dx[j], u[1] + dy[j])
            if 0 <= v[0] < M and 0 <= v[1] < N:
                vg = g[u[1]][u[0]]
                if sea[v[1]][v[0]] == 'G':
                    vg += 1
                elif sea[v[1]][v[0]] == 'P':
                    vg = 0
                if vg < g[v[1]][v[0]]:
                    g[v[1]][v[0]] = vg
                    heapq.heappush(queue, v)

    total = 0
    for h_point in herring:
        if g[h_point[1]][h_point[0]] < 4:
            total += 1

    print(f"Data Set {i + 1}:\n{total}\n")
