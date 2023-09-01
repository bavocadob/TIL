N = int(input())

dp = [0] * (N + 1)

# 처음에는 A만 누를 수 있음

#
for i in range(1, N + 1):
    dp[i] = dp[i - 1] + 1
    # 3개이전 칸부터 복사할 수 있으니까 3칸 이전칸부터 i칸 전칸까지 탐색하면서
    # 그때 복사한걸 계속 붙여넣었을때 뭐가 더 큰지를 비교
    for distance in range(3, i):
        dp[i] = max(dp[i], dp[i - distance] * (distance - 1))

print(dp[N])

