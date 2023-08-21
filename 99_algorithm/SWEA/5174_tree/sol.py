import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    E, N = map(int, input().split())

    child = [[0] * 2 for _ in range(E + 2)]
    edges = list(map(int, input().split()))

    for i in range(len(edges) // 2):
        if child[edges[i * 2]][0] == 0:
            child[edges[i * 2]][0] = edges[i * 2 + 1]
        else:
            child[edges[i * 2]][1] = edges[i * 2 + 1]

    visited = [False] * (E + 2)
    stack = [N]
    cnt = 1
    while stack:
        curr_node = stack.pop()

        if child[curr_node][0] != 0 and not visited[child[curr_node][0]]:
            stack.append(child[curr_node][0])
            visited[child[curr_node][0]] = True
            cnt += 1
        if child[curr_node][1] != 0 and not visited[child[curr_node][1]]:
            stack.append(child[curr_node][1])
            visited[child[curr_node][1]] = True
            cnt += 1

    print(f'#{tc+1} {cnt}')
