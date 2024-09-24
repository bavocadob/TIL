import sys

input = sys.stdin.readline


def build(left, right, node):
    if left == right:
        t[node] = nums[left]
        return

    mid = (left + right) // 2

    build(left, mid, node * 2)
    build(mid + 1, right, node * 2 + 1)
    t[node] = min(t[node * 2], t[node * 2 + 1])


def query(start, end, left, right, node):
    if left > end or right < start:
        return INF

    if start <= left and end >= right:
        return t[node]

    mid = (left + right) // 2

    return min(query(start, end, left, mid, node * 2), query(start, end, mid + 1, right, node * 2 + 1))


def update(idx, val, left, right, node):
    if left == right:
        t[node] = val
        return

    mid = (left + right) // 2

    if left <= idx <= mid:
        update(idx, val, left, mid, node * 2)
    else:
        update(idx, val, mid + 1, right, node * 2 + 1)

    t[node] = min(t[node * 2], t[node * 2 + 1])


N = int(input())
INF = int(1e9)
nums = list(map(int, input().split()))

t = [INF] * (N * 4)
build(0, N - 1, 1)

Q = int(input())

for _ in range(Q):
    cmd, a, b = map(int, input().split())
    if cmd == 1:
        update(a - 1, b, 0, N - 1, 1)
    else:
        print(query(a - 1, b - 1, 0, N - 1, 1))
