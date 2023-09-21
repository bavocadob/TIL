import sys

sys.stdin = open('input.txt')

INF = int(1e9)


def dijkstra(start):
    visited = [0] * (N + 1)
    distance = [INF] * (N + 1)
    distance[0] = 0

    for _ in range(N):
        next = 0
        min_dist = INF

        for i in range(N + 1):
            if not visited[i] and min_dist > distance[i]:
                next = i
                min_dist = distance[i]

        visited[next] = 1

        for j in range(N + 1):
            if not visited[j] and distance[j] > distance[next] + adj[next][j]:
                distance[j] = distance[next] + adj[next][j]

        print(visited, '방문')
        print(distance, '거리')

    return distance[N]


T = int(input())

for tc in range(T):
    N, E = map(int, input().split())

    adj = [[INF] * (N + 1) for _ in range(N + 1)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w

    print(f'#{tc + 1} {dijkstra(0)}')
