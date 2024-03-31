N, M, X = map(int, input().split())

adj = [[] for _ in range(N + 1)]
adj2 = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj2[b].append(a)


def dfs(root, adj_list):
    visited = [False] * (N + 1)
    cnt = 0
    queue = [root]

    while queue:
        temp = queue.pop()
        if not visited[temp]:
            visited[temp] = True
            cnt += 1
            for next_node in adj_list[temp]:
                if not visited[next_node]:
                    queue.append(next_node)
    return cnt - 1


cnt = dfs(X, adj)
reverse_cnt = dfs(X, adj2)

print(reverse_cnt + 1, N - cnt)
