import sys
from math import pi

input = sys.stdin.readline

T = int(input())
for t in range(T):
    N, K = map(int, input().split())

    cakes = []

    for _ in range(N):
        w, h = map(int, input().split())
        cakes.append((w, h))

    cakes.sort(reverse=True)

    cylinder = []
    base = []
    for i in range(N):
        w, h = cakes[i]
        base.append(w ** 2 + (2 * w * h))
        cylinder.append(((2 * w * h), i))
    cylinder.sort(reverse=True)

    ans = 0
    for i in range(N):
        temp = base[i]

        cnt = 1
        for j in range(N):
            if cnt == K:
                break
            c, idx = cylinder[j]
            if idx <= i:
                continue
            temp += c
            cnt += 1

        ans = max(ans, temp)

    print(f'Case #{t + 1}: {ans * pi}')
