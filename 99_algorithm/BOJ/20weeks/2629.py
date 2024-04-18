N = int(input())

A = list(map(int, input().split()))

M = sum(A)

dp = [[False] * (M + 1) for _ in range(N + 1)]

dp[0][0] = True

for i in range(1, N + 1):
    num = A[i - 1]
    for j in range(M + 1):
        if dp[i - 1][j]:
            dp[i][abs(j - num)] = True

    for j in range(M + 1, num - 1, -1):
        if dp[i - 1][j - num]:
            dp[i - 1][j] = True

    for j in range(M + 1):
        if dp[i - 1][j]:
            dp[i][j] = True

K = int(input())

B = list(map(int, input().split()))

ans = []

for num in B:
    if num > M:
        ans.append('N')
        continue
    ans.append('Y' if dp[N][num] else 'N')

print(*ans)
