N = int(input())

numbers = list(map(int, input().split()))

dp = [1] * N

for i in range(N):
    for j in range(i - 1, -1, -1):
        if numbers[i] > numbers[j]:
            dp[i] = max(1 + dp[j], dp[i])

print(max(dp))
