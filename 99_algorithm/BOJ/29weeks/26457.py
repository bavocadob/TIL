import sys

input = sys.stdin.readline

S, N = map(int, input().split())

students = []

for _ in range(S):
    a, h = map(int, input().split())
    students.append((h, a))

students.sort()

dp = [[0] * N for _ in range(S + 1)]

ans = 0

for i in range(S):

    if i >= N:
        ans = max(ans, dp[i - 1][N - 1] + students[i][1] - students[i][0])

    dp[i][1] = max(dp[i - 1][1], students[i][0] + students[i][1])
    for j in range(2, min(i + 1, N)):
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + students[i][1])

print(ans)
