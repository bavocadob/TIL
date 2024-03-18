import sys

input = sys.stdin.readline


def is_valid(target, arr, size):
    cnt = 1

    curr = arr[0]

    for i in range(1, N):
        if arr[i] - curr >= target:
            curr = arr[i]
            cnt += 1

    return cnt >= size


T = int(input())

for _ in range(T):
    N, S = map(int, input().split())
    pos = list(map(int, input().split()))
    pos.sort()
    left = 0
    right = pos[-1]

    while left <= right:
        mid = (left + right) // 2

        if is_valid(mid, pos, S):
            left = mid + 1
        else:
            right = mid - 1

    print(right)
