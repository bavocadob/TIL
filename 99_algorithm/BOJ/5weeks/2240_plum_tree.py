plum_dict = {1: 2, 2: 1}

time, move = map(int, input().split())

# 나무위치, 시간, 이동횟수

dp = [[[0] * move for _ in range(time)] for _ in range(2)]

plums = [int(input()) for _ in range(time)]

for t in range(time):
    for m in range(move):
        plum = plums[t]
        if plum == 1:
            dp[0][t][m] = max(dp[0][t - 1][m], dp[1][t - 1][m - 1]) + 1
            dp[1][t][m] = max(dp[1][t - 1][m], dp[0][t - 1][m - 1])
        else:
            dp[1][t][m] = max(dp[1][t - 1][m], dp[0][t - 1][m - 1]) + 1
            dp[0][t][m] = max(dp[0][t - 1][m], dp[1][t - 1][m - 1])

print(dp[0])
print(dp[1])
