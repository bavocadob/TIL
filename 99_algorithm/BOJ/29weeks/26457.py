import sys

input = sys.stdin.readline

S, N = map(int, input().split())

students = []

for _ in range(S):
    a, h = map(int, input().split())
    students.append((h, a))

students.sort()

dp = [[0] * (N + 1) for _ in range(S + 1)]

ans = 0

for i in range(1, S + 1):

    ans = max(ans, dp[i - 1][N - 1] + students[i - 1][1] - students[i - 1][0])

    dp[i][1] = max(dp[i - 1][1], students[i - 1][0] + students[i - 1][1])
    for j in range(2, N + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + students[i - 1][1])

print(ans)
