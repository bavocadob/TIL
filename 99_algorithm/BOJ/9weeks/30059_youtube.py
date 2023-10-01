import sys

input = sys.stdin.readline

INF = float('inf')

N, K = map(int, input().split())

youtube = [list() for _ in range(3)]

for _ in range(N):
    category, length = map(int, input().split())
    youtube[category].append(length)

if len(youtube[1]) + len(youtube[2]) * 2 < K:
    print(-1)
elif len(youtube[1]) + len(youtube[2]) * 2 == K:
    print(sum(youtube[1]) + sum(youtube[2]))
else:
    youtube[1].sort()
    youtube[2].sort()

    dp = [INF] * (K + 1)
    dp[0] = 0

    for i in range(1, len(youtube[2])):
        youtube[2][i] += youtube[2][i - 1]

    for i in range(1, min(len(youtube[1]), K) + 1):
        # print(i)
        dp[i] = dp[i - 1] + youtube[1][i - 1]

    for i in range(len(youtube[2])):
        distance = (i + 1) * 2
        if K - distance >= 0:
            dp[K] = min(dp[K], dp[K - distance] + youtube[2][i])
        elif K - distance == -1:
            dp[K] = min(dp[K], dp[0] + youtube[2][i])
        else:
            break

    print(dp[K])
