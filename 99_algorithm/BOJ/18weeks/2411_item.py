import sys

input = sys.stdin.readline

N, M, A, B = map(int, input().split())

items = []
dp = [[0] * M for _ in range(N)]

for _ in range(A):
    x, y = map(lambda k: int(k) - 1, input().split())
    items.append((x, y))

for _ in range(B):
    x, y = map(lambda k: int(k) - 1, input().split())
    dp[x][y] = -1

items.sort()
items.append((N - 1, M - 1))

dp[0][0] = 1

rst = []
curr_x, curr_y = 0, 0
for k in range(A + 1):
    x, y = items[k]

    for i in range(curr_x, x + 1):
        for j in range(curr_y, y + 1):
            if (i == curr_x and j == curr_y) or dp[i][j] == -1:
                continue
            if 0 <= i - 1 < N and 0 <= j < M and dp[i - 1][j] != -1:
                dp[i][j] += dp[i - 1][j]

            if 0 <= i < N and 0 <= j - 1 < M and dp[i][j - 1] != -1:
                dp[i][j] += dp[i][j - 1]

    rst.append(dp[i][j])
    dp[i][j] = 1
    curr_x, curr_y = x, y

ans = 1
for a in rst:
    ans *= a

print(ans)
