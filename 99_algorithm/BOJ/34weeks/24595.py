import sys

input = sys.stdin.readline


def solve(num):
    idx = 1

    while idx < len(num):
        if num[idx] >= num[idx - 1]:
            idx += 1
        else:
            break

    while idx < len(num):
        if num[idx] <= num[idx - 1]:
            idx += 1
        else:
            break

    for i in range(idx, len(num)):
        num[i] = num[i - 1]

    return ''.join(num)


T = int(input())

for _ in range(T):
    print(solve(list(input().rstrip())))
