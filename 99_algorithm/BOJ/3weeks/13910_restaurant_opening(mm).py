target, N = map(int, input().split())

woks = list(map(int, input().split()))
woks_list = [0] * 20001

dp = [10000000] * (target + 1)
dp[0] = 0



for i in range(0, N):
    woks_list[woks[i]] = 1
    for j in range(i + 1, N):
        woks_list[woks[i] + woks[j]] = 1

# print(woks_list)

for i in range(1, target + 1):
    if not woks_list[i]:
        continue

    for j in range(i, target + 1):
        dp[j] = min(dp[j], dp[j - i] + 1)

if dp[target] != 10000000:
    print(dp[target])
else:
    print(-1)

