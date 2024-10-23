import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
ans = n - 2

for i in range(n):
    for j in range(i + 1, n):
        if abs(a[j] - a[i]) % (j - i) == 0:
            d = (a[j] - a[i]) // (j - i)
            cnt = 0

            for k in range(n):
                need = a[i] + (k - i) * d
                if a[k] != need:
                    cnt += 1

            ans = min(ans, cnt)

print(ans)
