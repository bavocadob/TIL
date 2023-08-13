

target, N = map(int, input().split())

information = []

for _ in range(N):
    x, y = map(int, input().split())
    information.append((x, y))

dp_size = target + 100
dp = [int(1e9)] * dp_size
dp[0] = 0

for c, p in information:
    for i in range(p, dp_size):
        if dp[i - p] != int(1e9):
            dp[i] = min(dp[i], dp[i - p] + c)


result = int(1e9)
for i in range(target, dp_size):
    result = min(result, dp[i])

print(result)
