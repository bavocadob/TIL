import sys

input = sys.stdin.readline

N = int(input())

A = []
B = []

for _ in range(N):
    a, b = map(int, input().split())

    A.append(a)
    B.append(b)

A.sort()
B.sort()

ans = 0

for i in range(N):
    ans += abs(i + 1 - A[i])
    ans += abs(i + 1 - B[i])

print(ans)
