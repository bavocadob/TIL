import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = input().rstrip()
B = input().rstrip()

dp = [[0] * M for _ in range(N)]
ans = 0

for j in range(M):
    for i in range(N):
        if j == 0:
            dp[i][j] = 1 if A[i] == B[j] else 0
        else:
            if i > 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1])

            if i < N - 1:
                dp[i][j] = max(dp[i][j], dp[i + 1][j - 1])

            if A[i] == B[j]:
                dp[i][j] += 1

        ans = max(ans, dp[i][j])

print(ans)
