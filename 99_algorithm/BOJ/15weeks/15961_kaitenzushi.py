import sys

input = sys.stdin.readline

n, d, k, c = map(int, input().split())

sushi = [int(input()) for _ in range(n)]

V = [0] * (d + 1)

ans = 0
cnt = 0

for i in range(k):
    if not V[sushi[i]]:
        cnt += 1
    V[sushi[i]] += 1

for i in range(n):
    j = (i + k) % n

    V[sushi[i]] -= 1
    if not V[sushi[i]]:
        cnt -= 1

    if not V[sushi[j]]:
        cnt += 1
    V[sushi[j]] += 1

    temp = cnt
    if not V[c]:
        temp += 1

    ans = max(temp, ans)

print(ans)
