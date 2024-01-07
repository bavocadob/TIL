N = int(input())

A = list(map(int, input().split()))

A.sort()

if N == 1:
    print(A[0])
else:
    print(max(A[-2], sum(A) / N))
