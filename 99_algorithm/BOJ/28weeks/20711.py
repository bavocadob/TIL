import sys

input = sys.stdin.readline

N = int(input())

ans = 0

dp = [0] * 100_001

for _ in range(N):
    _, *peoples = map(int, input().split())

    temp = 0
    for people in peoples:
        temp = max(temp, dp[people])

    for people in peoples:
        dp[people] = temp + 1

    ans = max(ans, temp + 1)

print(ans)
