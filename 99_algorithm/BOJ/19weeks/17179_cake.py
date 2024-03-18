import sys

input = sys.stdin.readline


def is_valid(target, cnt):
    temp_cnt = 0

    curr = 0

    for p in point:
        if p - curr >= target:
            curr = p
            temp_cnt += 1

    return temp_cnt >= cnt + 1


def solve(cnt):
    left = 0
    right = K

    while left <= right:
        mid = (left + right) // 2
        if is_valid(mid, cnt):
            left = mid + 1
        else:
            right = mid - 1

    return left - 1


N, M, K = map(int, input().split())

point = [int(input()) for _ in range(M)]

point.append(K)

for _ in range(N):
    print(solve(int(input())))
