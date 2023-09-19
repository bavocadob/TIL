import sys

input = sys.stdin.readline
H, N = map(int, input().split())

dp = [0] * (H + 1)
dp[0] = 1

for _ in range(N):
    kilogram = int(input())
    for i in range(H, kilogram - 1, -1):
        if dp[i - kilogram]:
            dp[i] = 1

for i in range(H, -1, -1):
    if dp[i]:
        print(i)
        break
# print(dp)
