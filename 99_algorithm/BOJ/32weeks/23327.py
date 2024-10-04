import sys

input = sys.stdin.readline
N, Q = map(int, input().split())

A = list(map(int, input().split()))

popular = [0]
funny = [0]

for i in range(N):
    popular.append(popular[-1] + A[i])
    funny.append(funny[-1] + A[i] * popular[i])

for _ in range(Q):
    l, r = map(int, input().split())

    temp = funny[r] - funny[l - 1]
    temp -= (popular[r] - popular[l - 1]) * popular[l - 1]
    print(temp)
