import sys

input = sys.stdin.readline

N, D, money = map(int, input().split())

size = list(map(int, input().split()))

for _ in range(D - 1):
    value = list(map(int, input().split()))
    dp = [-1] * (money + 1)
    dp[0] = 0

    for i in range(N):
        curr_val = size[i]
        for j in range(curr_val, money + 1):
            if dp[j - curr_val] != -1:
                dp[j] = max(dp[j], dp[j - curr_val] + value[i])
    temp = 0
    for i in range(money + 1):
        temp = max(temp, money - i + dp[i])
    money = temp
    size = value

print(money)
