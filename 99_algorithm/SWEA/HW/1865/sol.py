import sys

sys.stdin = open('input.txt')

T = int(input())


def backtrack(depth, percentage):
    global ans
    if depth == N:
        ans = percentage
        return

    for i in range(N - 1, -1, -1):
        if visited[i] == 0:
            p = percentage * (work[depth][i] / 100)
            if p > ans:
                visited[i] = True
                backtrack(depth + 1, p)
                visited[i] = False


for tc in range(T):
    N = int(input())
    visited = [0] * (N + 1)
    ans = 0
    work = [list(map(int, input().split())) for _ in range(N)]
    backtrack(0, 1)
    print(f'#{tc + 1} {ans * 100:.7f}')
