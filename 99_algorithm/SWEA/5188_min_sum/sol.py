import sys

sys.stdin = open('input.txt')

dx = [1, 0]
dy = [0, 1]


def valid(x, y):
    return 0 <= x < N and 0 <= y < N


def dfs(x, y, val):
    global result
    if val > result:
        return

    if (x, y) == (N - 1, N - 1):
        result = val
        return

    for k in range(2):
        nx, ny = x + dx[k], y + dy[k]
        if valid(nx, ny):
            dfs(nx, ny, val + numbers[nx][ny])


T = int(input())

for tc in range(T):
    N = int(input())

    numbers = [list(map(int, input().split())) for _ in range(N)]

    result = float('inf')

    dfs(0, 0, numbers[0][0])
    print(f'#{tc + 1} {result}')
