import sys
from collections import deque

input = sys.stdin.readline

queue = deque()

N, M, T = map(int, input().split())

_map = [list(input().rstrip()) for _ in range(N)]
r1, c1, r2, c2 = map(lambda x: int(x) - 1, input().split())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dp = [[[0] * (T + 1) for _ in range(M)] for _ in range(N)]

dp[r1][c1][0] = 1

for t in range(1, T + 1):
    for i in range(N):
        for j in range(M):
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]

                if not (0 <= nx < N and 0 <= ny < M) or _map[nx][ny] == '*':
                    continue

                dp[i][j][t] += dp[nx][ny][t - 1]

print(dp[r2][c2][T])