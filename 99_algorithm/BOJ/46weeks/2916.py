import sys

input = sys.stdin.readline
MOD = 360

N, K = map(int, input().split())

A = list(map(int, input().split()))

dp = [0] * 361
dp[0] = 1

for angle in A:
    temp = dp[:]
    for i in range(360):
        if dp[i] == 0:
            continue

        for j in range(1, 360):
            temp[(i + (j * angle)) % MOD] = 1
            temp[abs(i - (j * angle)) % MOD] = 1
    dp = temp


for q in list(map(int, input().split())):
    print('YES' if dp[q] else 'NO')
