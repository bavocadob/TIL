import sys

input = sys.stdin.readline
INF = int(1e9)


def dijkstra():
    distances = [[INF] * (K + 1) for _ in range(N + 1)]
    distances[1][0] = 0

    for cnt in range(K + 1):
        for node in range(1, N + 1):
            if distances[node][cnt] == INF:
                continue

            for next_node, cost, gap in adj[node]:
                next_time = distances[node][cnt] + gap - (distances[node][cnt] % gap) + cost
                if distances[node][cnt] % gap == 0:
                    next_time -= gap

                if next_time < distances[next_node][cnt]:
                    distances[next_node][cnt] = next_time

                if cnt < K:
                    next_time = distances[node][cnt] + cost
                    if next_time < distances[next_node][cnt + 1]:
                        distances[next_node][cnt + 1] = next_time

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
