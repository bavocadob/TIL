import sys

input = sys.stdin.readline


def build(t, left, right, node):
    if left == right:
        if numbers[left] % 2:
            t[node] = (1, 0)
        else:
            t[node] = (0, 1)
        return

    mid = (left + right) // 2

    build(t, left, mid, node * 2)
    build(t, mid + 1, right, node * 2 + 1)
    t[node] = (t[node * 2][0] + t[node * 2 + 1][0], t[node * 2][1] + t[node * 2 + 1][1])


def update(t, idx, val, left, right, node):
    if left == right:
        if val % 2:
            t[node] = (1, 0)
        else:
            t[node] = (0, 1)
        return

    mid = (left + right) // 2

    if left <= idx <= mid:
        update(t, idx, val, left, mid, node * 2)
    else:
        update(t, idx, val, mid + 1, right, node * 2 + 1)

    a, b = t[node * 2]
    c, d = t[node * 2 + 1]
    t[node] = (a + c, b + d)


def query(t, start, end, left, right, node):
    if left > end or right < start:
        return 0, 0

    if left >= start and right <= end:
        return t[node]

    mid = (left + right) // 2

    a, b = query(t, start, end, left, mid, node * 2)
    c, d = query(t, start, end, mid + 1, right, node * 2 + 1)
    return a + c, b + d


N = int(input())

numbers = list(map(int, input().split()))

tree = [(0, 0)] * (N * 4)
build(tree, 0, N - 1, 1)

Q = int(input())

for _ in range(Q):
    cmd, a, b = map(int, input().split())
    if cmd == 1:
        update(tree, a - 1, b, 0, N - 1, 1)
    else:
        odd, even = query(tree, a - 1, b - 1, 0, N - 1, 1)
        if cmd == 2:
            print(even)
        else:
            print(odd)
