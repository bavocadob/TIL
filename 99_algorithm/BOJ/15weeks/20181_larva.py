N, K = map(int, input().split())

foods = list(map(int, input().split()))
dp = [0] * (N + 1)
left = right = ans = temp = 0

while right < N:
    temp += foods[right]
    dp[right] = dp[right - 1]
    while temp >= K:
        dp[right] = max(dp[right], temp - K + dp[left - 1])
        temp -= foods[left]
        left += 1

    right += 1

print(dp[N - 1])
