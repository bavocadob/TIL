import sys

input = sys.stdin.readline

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]


def infect(x, y):
    queue = [(x, y)]

    visited = [[False] * M for _ in range(N)]

    while queue:
        x, y = queue.pop()

        if A[x][y] < 'D':
            A[x][y] = chr(ord(A[x][y]) + 1)
        elif not visited[x][y]:
            visited[x][y] = True
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < N and 0 <= ny < M and A[nx][ny] != 'X' and not visited[nx][ny]:
                    queue.append((nx, ny))


T = int(input())

for _ in range(T):
    M, N = map(int, input().split())

    A = [list(input().strip()) for _ in range(N)]

    K = int(input())

    for _ in range(K):
        b, a = map(int, input().split())
        infect(a, b)

    print('\n'.join([''.join(aa) for aa in A]))

    del A, M, N, K
