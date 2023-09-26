import sys

sys.stdin = open('input.txt')

T = int(input())


def backtrack(depth, val):
    global min_costs
    if val > min_costs:
        return

    if depth == N:
        min_costs = val
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            backtrack(depth + 1, val + costs[depth][i])
            visited[i] = False


for tc in range(T):
    N = int(input())

    costs = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_costs = int(1e9)
    backtrack(0, 0)
    print(f'#{tc + 1} {min_costs}')
