import sys


def dfs(idx, val, depth):
    global min_cost
    if val > min_cost:
        return

    if depth == N:
        min_cost = min(min_cost, val + cost[idx][0])
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(i, val + cost[idx][i], depth + 1)
            visited[i] = False


sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())

    cost = [list(map(int, input().split())) for _ in range(N)]

    min_cost = float('inf')

    visited = [False] * N
    visited[0] = True
    dfs(0, 0, 1)
    print(f'#{tc + 1} {min_cost}')
