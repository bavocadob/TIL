import sys

input = sys.stdin.readline
N, M, K = map(int, input().split())

A = [0, 0, 0, 0]
for _ in range(K):
    a, b = map(int, input().split())

    if (a + b) % 2:
        A[a % 2] = 1
    else:
        A[(a % 2) + 2] = 1

if sum(A) == 4:
    print('YES')
else:
    print('NO')
