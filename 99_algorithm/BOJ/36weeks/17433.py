import sys

input = sys.stdin.readline
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()
    for i in range(1, N):
        A[i - 1] = A[i] - A[i - 1]

    A = A[:-1]

    tmp = set()
    for i in range(1, N - 1):
        if A[i] != 0:
            tmp.add(gcd(A[0], A[i]))

    if not tmp:
        print("INFINITY")
    else:
        print(min(tmp))
