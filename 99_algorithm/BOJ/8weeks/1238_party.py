import sys

input = sys.stdin.readline

N, D = map(int, input().split())

dp = [i for i in range(D + 1)]

road = []
for _ in range(N):
    left, right, cost = map(int, input().split())
    road.append([left, right, cost])

road.sort(key=lambda x: x[1])

for i in range(N):
    left, right, cost = road[i]
    if right > D or dp[left] + cost > dp[right]:
        continue

    dp[right] = dp[left] + cost

    for i in range(right + 1, D + 1):
        if dp[i] >= dp[i - 1] + 1:
            dp[i] = dp[i - 1] + 1
        else:
            break

print(dp[D])
