import sys

input = sys.stdin.readline

T = int(input())
INF = int(1e9)

for tc in range(T):
    N, M, W = map(int, input().split())

    adj = [list() for _ in range(N + 1)]
    distances = [INF] * (N + 1)
    distances[1] = 0
    for _ in range(M):
        v, e, p = map(int, input().split())
        adj[v].append((e, p))
        adj[e].append((v, p))

    for _ in range(W):
        v, e, p = map(int, input().split())
        adj[v].append((e, -p))

    has_cycle = False

    for i in range(N):

        update = False
        for v in range(1, N + 1):
            # if distances[v] == INF:
            #     continue

            for next_node, weight in adj[v]:
                if (distance := distances[v] + weight) < distances[next_node]:
                    distances[next_node] = distance
                    update = True

        if not update:
            break

        if i == N - 1 and update:
            has_cycle = True

    if has_cycle:
        print('YES')
    else:
        print('NO')
