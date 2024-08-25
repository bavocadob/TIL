import sys

input = sys.stdin.readline
N = int(input())

A = [i for i in range(1, N + 1, 2)] + [i for i in range(2, N + 1, 2)]

A[3], A[(N - 1) // 2] = A[(N - 1) // 2], A[3]
A[(N + 1) // 2 + 3], A[N - 1] = A[N - 1], A[(N + 1) // 2 + 3]

rst = [A]

for i in range(N - 1):
    rst.append(rst[i][1:] + rst[i][:1])

for r in rst:
    print(*r)
