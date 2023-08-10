# 백준 2156 포도주시식
# 동적계획법

# 세개 연속으로 못마신다 = 1칸 + 2칸 or 2칸 + 1칸씩 마셔야함
# 1칸 + 2칸 = 이전꺼 와인양 + 3칸전꺼 최대

import sys
input = sys.stdin.readline

N = int(input())

wine = []

for _ in range(N):
    wine.append(int(input()))

if N == 1:
    print(wine[0])
else:
    dp = [0] * (N + 1)
    dp[1], dp[2] = wine[0], wine[1] + wine[0]

    for i in range(3, N + 1):
        a = wine[i - 1] + dp[i - 2]
        b = wine[i - 1] + wine[i - 2] + dp[i - 3]

        dp[i] = max(a, b, dp[i - 1])

    print(dp)