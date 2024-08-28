import sys

input = sys.stdin.readline
N, T = map(int, input().split())

A = [0] + [int(input()) for _ in range(N)]

acc = 0

for i in range(1, N + 1):
    acc += A[i]
    ans = 1

    A[i] = max(A[i], A[i - 1])

    if acc <= T:
        curr = T - acc + 1
        ans += curr // A[i] + (curr % A[i] != 0)

    print(ans)
