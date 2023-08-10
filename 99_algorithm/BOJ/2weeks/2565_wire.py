# 전깃줄
# 전봇대 1 ~ 500
# 오름차순으로 나타나는 최대 길이를 구하고 전깃줄의 개수에서 뺀다

N = int(input())

wire = [None] * 501

dp = [None] * 501

for i in range(N):
    x, y = map(int, input().split())
    wire[x] = y
    dp[x] = 1

for i in range(501):
    if wire[i] is not None:
        for j in range(i - 1, -1, -1):
            if wire[j] is not None and wire[i] > wire[j]:
                dp[i] = max(dp[j] + 1, dp[i])


max_val = 0
for i in range(501):
    if dp[i] is not None and dp[i] > max_val:
        max_val = dp[i]

print(N - max_val)