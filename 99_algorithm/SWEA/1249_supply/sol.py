import sys

sys.stdin = open('input.txt')

from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if dp[nx][ny] > dp[x][y] + road[x][y]:
                    dp[nx][ny] = dp[x][y] + road[x][y]
                    queue.append((nx, ny))


T = int(input())

for tc in range(T):
    N = int(input())
    road = [list(map(int, list(input()))) for _ in range(N)]
    dp = [[float('inf')] * N for _ in range(N)]
    dp[0][0] = 0

    bfs(0, 0)
    print(f'#{tc + 1} {dp[N-1][N-1]}')
