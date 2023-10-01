import sys

input = sys.stdin.readline

N = int(input())

domino = [list(map(int, input().split())) for _ in range(N)]
domino.sort()

to_right = [i for i in range(N)]
to_left = [i for i in range(N)]

for i in range(N):
    l = domino[i][0] - domino[i][1]
    for j in range(i - 1, -1, -1):
        if domino[j][0] >= l:
            l = min(l, domino[j][0] - domino[j][1])
            to_left[i] = min(to_left[i], j)

    r = domino[i][0] + domino[i][1]
    for j in range(i + 1, N):
        if domino[j][0] <= r:
            r = max(r, domino[j][0] + domino[j][1])
            to_right[i] = max(to_right[i], j)


dp = [int(1e9) for i in range(N)]

dp[0] = 1
for i in range(N):
    if to_left[i] == 0:
        dp[i] = min(dp[i], 1)
    else:
        dp[i] = min(dp[i], dp[to_left[i] - 1] + 1)

    for j in range(i):
        if to_right[j] >= i:
            if j == 0:
                dp[i] = min(dp[i], 1)
            else:
                dp[i] = min(dp[i], dp[j - 1] + 1)

    # if to_right[i] == to_right[i - 1]:
    #     dp[i] = min(dp[i - 1], dp[i])
    # else:
    #     dp[i] = min(dp[i - 1] + 1, dp[i])

# print(to_left)
# print(to_right)
print(dp[N - 1])
