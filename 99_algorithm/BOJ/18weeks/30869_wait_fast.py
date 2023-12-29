import sys

input = sys.stdin.readline
INF = int(1e9)


def dijkstra():
    distances = [[INF] * (K + 1) for _ in range(N + 1)]
    visited = [[False] * (K + 1) for _ in range(N + 1)]
    distances[1][0] = 0

    for _ in range(N):
        for k in range(K + 1):
            min_value = INF
            index = 0
            for i in range(1, N + 1):
                if not visited[i][k] and distances[i][k] < min_value:
                    min_value = distances[i][k]
                    index = i

            visited[index][k] = True

            for end, time, gap in adj[index]:
                mod = min_value % gap
                wait = (gap - mod) % gap
                if min_value + wait + time < distances[end][k]:
                    distances[end][k] = min_value + wait + time

                if k < K and distances[end][k + 1] > min_value + time:
                    distances[end][k + 1] = min_value + time

    ans = INF
    for i in range(K + 1):
        ans = min(ans, distances[N][i])

    if ans != INF:
        return ans
    else:
        return -1


N, M, K = map(int, input().split())

adj = [list() for _ in range(N + 1)]

for _ in range(M):
    s, e, t, g = map(int, input().split())
    adj[s].append((e, t, g))

print(dijkstra())
