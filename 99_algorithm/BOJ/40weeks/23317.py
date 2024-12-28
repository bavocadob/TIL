import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
coord = set()

for i in range(M):
    a, b = map(int, input().split())
    coord.add((a, b))

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

ans = 0

coord = sorted(list(coord), reverse=True)
while coord and coord[-1][0] == 0:
    coord.pop()

for i in range(1, N):
    flag = False
    x, y = -1, -1
    if coord and coord[-1][0] == i:
        flag = True
        x, y = coord.pop()
    elif coord and coord[-1][0] < i:
        break

    for j in range(i + 1):
        dp[i][j] += dp[i - 1][j]
        if j - 1 >= 0:
            dp[i][j] += dp[i - 1][j - 1]

        if flag and y != j:
            dp[i][j] = 0

ans = 0

for j in range(N):
    ans += dp[N - 1][j]

print(ans)
