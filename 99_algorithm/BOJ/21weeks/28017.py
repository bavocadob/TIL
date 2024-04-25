import sys

input = sys.stdin.readline

N, M = map(int, input().split())
dp = [0] * M

INF = int(1e9)

for _ in range(N):
    cur = [0] * M
    row = list(map(int, input().split()))

    for i in range(M):
        temp = INF
        for j in range(M):
            if i == j:
                continue
            temp = min(temp, dp[j])

        cur[i] = row[i] + temp

    dp = cur

print(min(dp))
