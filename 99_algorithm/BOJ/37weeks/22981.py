import math

N, K = map(int, input().split())

A = list(map(int, input().split()))

A.sort()

ans = 0
for i in range(1, N):
    temp = (A[0] * i) + (A[i] * (N - i))
    ans = max(ans, temp)

print(K // ans if K % ans == 0 else K // ans + 1)
