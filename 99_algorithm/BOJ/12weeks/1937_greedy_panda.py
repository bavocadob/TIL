import sys

input = sys.stdin.readline
sys.setrecursionlimit(200000)
mm = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N


def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]

    bamboo = bamboos[x][y]
    rst = 0

    for dx, dy in mm:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny) and bamboos[nx][ny] > bamboo:
            rst = max(dfs(nx, ny), rst)

    rst += 1
    dp[x][y] = rst
    return rst


N = int(input())

bamboos = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        ans = max(ans, dfs(i, j))

print(ans)
