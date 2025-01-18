import sys

input = sys.stdin.readline
N, M = map(int, input().split())

red = []
white = []
blue = []

for _ in range(N):
    red.append(list(map(int, input().split())))

for _ in range(N):
    white.append(list(map(int, input().split())))

for _ in range(N):
    blue.append(list(map(int, input().split())))

dp = [[[-1] * (1 << 3) for _ in range(M)] for _ in range(N)]

for i in range(M):
    dp[N - 1][i][0] = 0

for i in range(N):
    for j in range(M):
        for k in (2 ** ex for ex in range(3)):
            for x in range(1 << 3):
                if not (x & k):
                    continue

                temp = k >> 1
                flag = True
                while temp:
                    if not (temp & x):
                        flag = False

                    temp = temp >> 1

                temp = k << 1
                while temp < (1 << 3):
                    if temp & x:
                        flag = False

                    temp = temp << 1

                if not flag:
                    continue

                for y in range(1 << 3):
                    if (y | k) != x or dp[i - 1][j][y] == -1:
                        continue

                    temp = 0
                    if k == (1 << 0):
                        temp = red[i][j]
                    elif k == (1 << 1):
                        temp = white[i][j]
                    else:
                        temp = blue[i][j]

                    dp[i][j][x] = max(dp[i][j][x], dp[i - 1][j][y] + temp)

ans = 0

for i in range(M):
    ans += dp[N - 1][i][(1 << 3) - 1]

print(ans)
