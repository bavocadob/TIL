import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

damage = [int(input()) for _ in range(N)]
damage.sort()
boss = [list(map(int, input().split())) for _ in range(K)]

meso = 0
for i in range(N - M, N):
    dp = [-1] * 901
    dp[0] = 0

    for k in range(K):
        hp, money = boss[k]
        time = hp // damage[i]
        if hp % damage[i]:
            time += 1

        for j in range(900, time - 1, -1):
            if dp[j - time] != -1:
                dp[j] = max(dp[j], dp[j - time] + money)

    meso += max(dp)

print(meso)
