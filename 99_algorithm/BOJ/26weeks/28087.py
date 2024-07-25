import sys

input = sys.stdin.readline


def solve():
    rst = []

    temp = 0
    for i in range(M):
        if N <= A[i] <= N * 2:
            return [i + 1]

        if A[i] <= N:
            temp += A[i]
            rst.append(i + 1)

        if N <= temp <= N * 2:
            break

    return rst


N, M = map(int, input().split())

A = [int(input()) for _ in range(M)]

ans = solve()

print(len(ans))
for aa in ans:
    print(aa)
