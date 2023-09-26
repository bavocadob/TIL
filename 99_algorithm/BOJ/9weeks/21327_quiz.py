import sys

input = sys.stdin.readline

N, M, K, B = map(int, input().split())

categories = [[] for _ in range(M)]

for _ in range(N):
    p, c = map(int, input().split())
    categories[c - 1].append(p)

for i in range(M):
    categories[i].sort(reverse=True)
    for j in range(1, len(categories[i])):
        categories[i][j] += categories[i][j - 1]

dp = [[0] * (K + 1) for _ in range(M + 1)]

for m in range(1, M + 1):
    for k in range(1, K + 1):
        for i in range(len(categories[m - 1]) + 1):
            if k - i < 0:
                break

            inc = 0 if i == 0 else categories[m - 1][i - 1]
            if i == len(categories[m - 1]):
                inc += B
            dp[m][k] = max(dp[m][k], dp[m - 1][k - i] + inc)

print(dp[M][K])
