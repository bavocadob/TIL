def solution():
    def dfs(node):
        visited[node] = True
        cnt = 1
        for next_node in adj[node]:
            if not visited[next_node]:
                cnt += dfs(next_node)

        return cnt

    N = int(input())

    if N == 1:
        return 0

    adj = [list() for _ in range(N + 1)]

    adj_cnt = 0

    for i in range(1, N + 1):
        route = input().rstrip()

        for j, r in enumerate(route):
            if r == 'Y':
                adj[i].append(j + 1)
                adj_cnt += 1

    adj_cnt //= 2

    visited = [False] * (N + 1)

    area_cnt = 0
    # connect_cnt = 0
    for i in range(1, N + 1):
        if not visited[i]:
            area_cnt += 1
            c = dfs(i)
            if c == 1:
                return -1

    if adj_cnt - (N - area_cnt) >= area_cnt - 1:
        return area_cnt - 1
    else:
        return -1


print(solution())
