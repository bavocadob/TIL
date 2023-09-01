import sys
input = sys.stdin.readline

time, move = map(int, input().split())

# 나무위치, 시간, 이동횟수
dp = [[0] * (time + 1) for _ in range(move + 1)]

for t in range(1, time + 1):
    plum = int(input())
    for m in range(move + 1):
        if m == 0:
            if plum == 1:
                dp[0][t] = dp[0][t - 1] + 1
            else:
                dp[0][t] = dp[0][t - 1]
        else:
            dp[m][t] = max(dp[m - 1][t - 1], dp[m][t - 1])
            if m % 2 == 0 and plum == 1:
                dp[m][t] += 1
            elif m % 2 and plum == 2:
                dp[m][t] += 1

result = 0

for d in dp:
    result = max(max(d), result)

print(result)
