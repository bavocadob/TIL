import sys

input = sys.stdin.readline


def solve():
    l = left[0]
    r = right[0]

    for k in range(1, N):
        if left[k] > r or right[k] < l:
            return 0

        l = max(left[k], l)
        r = min(right[k], r)
    if l > r:
        return 0

    return 1


N, T = map(float, input().split())
N = int(N)

pos = list(map(int, input().split()))
speed = list(map(int, input().split()))

left = [0.0] * N
right = [0.0] * N

for i in range(N):
    dist = speed[i] * T
    left[i] = round(pos[i] - dist, 4)
    right[i] = round(pos[i] + dist, 4)

print(solve()))