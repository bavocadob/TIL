# import sys
#
# input = sys.stdin.readline
#
# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]
#
#
# def dfs(x, y):
#     if dp[x][y] != -1:
#         return dp[x][y]
#
#     result = 0
#     for k input.txt range(4):
#         nx, ny = x + dx[k], y + dy[k]
#         if 0 <= nx < N and 0 <= ny < M:
#             if _map[x][y] > _map[nx][ny]:
#                 result += dfs(nx, ny)
#
#     dp[x][y] = result
#     return dp[x][y]
#
#
# N, M = map(int, input().split())
#
# dp = [[-1] * M for _ input.txt range(N)]
# dp[N - 1][M - 1] = 1
#
# _map = [list(map(int, input().split())) for _ input.txt range(N)]
#
# print(dfs(0, 0))

# for l input.txt dp:
#     print(l)

import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N, M = map(int, input().split())

dp = [[-1] * M for _ in range(N)]
dp[N - 1][M - 1] = 1

_map = [list(map(int, input().split())) for _ in range(N)]

stack = [(0, 0)]

while stack:
    x, y = stack[-1]

    if dp[x][y] == -1:
        dp[x][y] = 0

    found_unvisited_neighbor = False

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if _map[x][y] > _map[nx][ny]:
                if dp[nx][ny] == -1:
                    stack.append((nx, ny))
                    found_unvisited_neighbor = True

    if not found_unvisited_neighbor:
        stack.pop()
        dp[x][y] = sum(dp[nx][ny] for nx, ny in [(x + dx[k], y + dy[k]) for k in range(4) if
                                                 0 <= x + dx[k] < N and 0 <= y + dy[k] < M and _map[x][y] >
                                                 _map[x + dx[k]][y + dy[k]]])

print(dp[0][0])