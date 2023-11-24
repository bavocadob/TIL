from bisect import bisect_left

N = int(input())

A = list(map(int, input().split()))
A.sort()
ans = 0
for i in range(N - 2):
    l, r = i + 1, N - 1
    while l < r:
        temp = A[i] + A[l] + A[r]
        if temp > 0:
            r -= 1
        elif temp < 0:
            l += 1
        else:
            if A[l] == A[r]:
                ans += r - l
            else:
                ans += r - bisect_left(A, A[r]) + 1
            l += 1
print(ans)
