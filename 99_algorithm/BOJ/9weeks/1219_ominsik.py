import sys

input = sys.stdin.readline


def dfs(start, end, graph):
    visited = [False] * N
    visited[start] = True

    stack = [start]

    while stack:
        node = stack.pop()
        if node == end:
            return True

        for n_node, _ in graph[node]:
            if not visited[n_node]:
                visited[n_node] = True
                stack.append(n_node)

    return False


def check_to_end(node):
    return dfs(node, E, adj) or dfs(node, E, reverse_adj)


N, S, E, M = map(int, input().split())

INF = int(1e9)
adj = [list() for _ in range(N)]
reverse_adj = [list() for _ in range(N)]
for _ in range(M):
    v, e, p = map(int, input().split())
    adj[v].append((e, p))
    reverse_adj[e].append((v, p))

costs = list(map(int, input().split()))
distances = [INF] * N
distances[S] = -costs[S]

has_cycle = False

for i in range(N):
    update = False
    update_idx = None
    for v in range(N):
        if distances[v] != INF:
            for next_node, weight in adj[v]:
                next_cost = distances[v] + weight - costs[next_node]
                if next_cost < distances[next_node]:
                    distances[next_node] = next_cost
                    update = True
                    update_idx = next_node

    if not update:
        break

    if i == N - 1 and update:
        has_cycle = check_to_end(update_idx)

if distances[E] == INF:
    print('gg')
else:
    if has_cycle:
        print('Gee')
    else:
        print(distances[E] * -1)
