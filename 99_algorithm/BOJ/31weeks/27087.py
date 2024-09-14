import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b, c, p = map(int, input().split())

    cnt = 0

    if not a % p: cnt += 1
    if not b % p: cnt += 1
    if not c % p: cnt += 1

    if cnt >= 2:
        print(1)
    else:
        print(0)
