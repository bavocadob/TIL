def dfs(start, adj):
    stack = [start]
    distance = [0] * len(adj)
    distance[start] = 1
    max_dist = 0
    root_node = 0

    while stack:
        node = stack.pop()
        for next_node in adj[node]:
            if not distance[next_node]:
                distance[next_node] = distance[node] + 1
                stack.append(next_node)
                if distance[next_node] > max_dist:
                    max_dist = distance[next_node]
                    root_node = next_node

    return max_dist, root_node


def getMaxTime(g_nodes, g_from, g_to):
    if g_nodes == 1:
        return 0

    adj = [list() for _ in range(g_nodes + 1)]

    for i in range(g_nodes - 1):
        a, b = g_from[i], g_to[i]
        adj[a].append(b)
        adj[b].append(a)

    _, root = dfs(1, adj)
    result, _ = dfs(root, adj)

    return result - 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i] = map(int, input().rstrip().split())

    result = getMaxTime(g_nodes, g_from, g_to)

    fptr.write(str(result) + '\n')

    fptr.close()