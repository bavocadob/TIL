import sys

input = sys.stdin.readline

N, M = map(int, input().split())
INF = int(1e9)

distances = [INF] * (N + 1)
distances[1] = 0
has_cycle = False

adj = [list() for _ in range(N + 1)]

for _ in range(M):
    v, e, p = map(int, input().split())
    adj[v].append((e, p))

for iter in range(N):
    update = False

    for v in range(1, N + 1):
        if distances[v] == INF:
            continue

        for e, p in adj[v]:
            if (distance := distances[v] + p) < distances[e]:
                distances[e] = distance
                update = True

    if not update:
        break

    if update and iter == N - 1:
        has_cycle = True

if has_cycle:
    print(-1)
else:
    for i in range(2, N + 1):
        if distances[i] == INF:
            print(-1)
        else:
            print(distances[i])
