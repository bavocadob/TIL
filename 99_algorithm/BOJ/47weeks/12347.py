def check(f, r):
    global ans
    g = r - f
    cur = r * 10 + f
    while cur <= N:
        ans += 1
        r += g
        if r < 0 or r > 9:
            break
        cur = cur * 10 + r


N = int(input())

ans = 9 if N >= 10 else N % 10

for first in range(1, 10):
    for i in range(10):
        check(first, i)

print(ans)
