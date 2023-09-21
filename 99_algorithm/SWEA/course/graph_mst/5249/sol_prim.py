import heapq

T = int(input())


def mst(idx):
    pq = []

    visited = [0] * (V + 1)
    visited[idx] = True

    for next in adj[idx]:
        weight, n_idx = next
        heapq.heappush(pq, (weight, n_idx))

    ans = 0

    while pq:
        weight, idx = heapq.heappop(pq)

        if visited[idx]:
            continue

        visited[idx] = True
        ans += weight

        for next in adj[idx]:
            weight, n_idx = next
            if not visited[n_idx]:
                heapq.heappush(pq, (weight, n_idx))

    return ans


for tc in range(T):
    V, E = map(int, input().split())

    adj = [list() for _ in range(V + 1)]

    for _ in range(E):
        x, y, w = map(int, input().split())
        adj[x].append((w, y))
        adj[y].append((w, x))

    print(f'#{tc + 1} {mst(0)}')
