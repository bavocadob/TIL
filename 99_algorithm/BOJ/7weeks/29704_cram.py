import sys

input = sys.stdin.readline

N, T = map(int, input().split())

dp = [-1] * (T + 1)
dp[0] = 0
max_fine = 0

report = []
for i in range(N):
    x, y = map(int, input().split())
    max_fine += y
    report.append((x, y))

for i in range(N):
    day, fine = report[i]
    for j in range(T, day - 1, -1):
        if dp[j - day] != -1:
            dp[j] = max(dp[j], dp[j - day] + fine)

# print(max_fine, dp)
print(max_fine - max(dp))
