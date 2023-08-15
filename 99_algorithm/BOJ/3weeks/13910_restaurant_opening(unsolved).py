target, N = map(int, input().split())

woks = list(map(int, input().split()))

visited = [False] * N

woks_set = set(woks)



dp = [-1] * (target + 1)
dp[0] = 0

for wok in woks_set:
    for i in range(wok, target + 1):
        if dp[i] == -1 and dp[i - wok] != -1:
            dp[i] = dp[i - wok] + 1
        elif dp[i] != - 1 and dp[i - wok] != -1:
            dp[i] = min(dp[i], dp[i - wok] + 1)

print(dp[target])
