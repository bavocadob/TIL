N, K = map(int, input().split())

A = list(map(int, input().split()))

l = 0
ans = 0
for i in range(N):
    if l < 0:
        l = i
    if (K | A[i]) > K:
        ans = 0
        l = -1
        r = -1
    else:
        ans = A[i] | ans
        if ans == K:
            r = i
            break

if ans == K:
    print(l + 1, r + 1)
else:
    print(-1)
