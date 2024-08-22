import sys

input = sys.stdin.readline


def is_valid_offset(dx, dy, target, A):
    for tx, ty in target:
        if (tx + dx, ty + dy) not in A:
            return False
    return True


M = int(input())
target = [tuple(map(int, input().rstrip().split())) for _ in range(M)]
N = int(input())
A = set(tuple(map(int, input().rstrip().split())) for _ in range(N))

tx0, ty0 = target[0]

for ax, ay in A:
    dx, dy = ax - tx0, ay - ty0

    if is_valid_offset(dx, dy, target, A):
        print(dx, dy)
        break
