N = int(input())
yukgaksu = [1]

i = 1
while yukgaksu[-1] < N:
    yukgaksu.append((i + 1) * (i * 2 + 1))
    i += 1

# DP 배열 초기화
dp = [i for i in range(N + 1)]

for num in yukgaksu:
    for j in range(num, N + 1):
        dp[j] = min(dp[j], dp[j - num] + 1)

print(dp[N])
