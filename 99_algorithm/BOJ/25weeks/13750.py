import sys

input = sys.stdin.readline


N = int(input())

A = [int(input()) for _ in range(N)]

ans = 1
d = 0
prev = A[0]

for i in range(N):
    if A[i] != prev:
        temp_d = A[i] - prev
        if d == 0 or d * temp_d < 0:
            ans += 1

        prev = A[i]
        d = temp_d

print(ans)
