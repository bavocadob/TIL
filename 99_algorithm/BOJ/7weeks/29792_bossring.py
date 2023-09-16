N, M, K = map(int, input().split())

damage = [int(input()) for _ in range(N)]
boss = [list(map(int, input().split())) for _ in range(K)]

meso = 0
for i in range(N - M, N):
    dp = [-1] * 1501
    dp[0] = 0

    for k in range(K):
        hp, money = boss[k]
        time = hp // damage[i]
        if hp % damage[i]:
            time += 1

        for j in range(1500, time - 1, -1):
            if dp[j - time] != -1:
                dp[j] = max(dp[j], dp[j - time] + money)
    for d in range(15):
        print(dp[d * 100: d * 100 + 101])


    meso += max(dp)

print(meso)
