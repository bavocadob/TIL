import sys

input = sys.stdin.readline


def build(arr, t, node, left, right):
    if left == right:
        t[node] = arr[left]
        return t[node]

    mid = (left + right) // 2
    left_val = build(arr, t, node * 2, left, mid)
    right_val = build(arr, t, node * 2 + 1, mid + 1, right)
    t[node] = left_val + right_val
    return t[node]


def query(t, start, end, node, left, right):
    if left >= start and right <= end:
        return t[node]

    if start > right or end < left:
        return 0

    mid = (left + right) // 2
    left_val = query(t, start, end, node * 2, left, mid)
    right_val = query(t, start, end, node * 2 + 1, mid + 1, right)

    return left_val + right_val


def update(t, idx, val, node, left, right):
    if idx < left or idx > right:
        return t[node]

    if left == right:
        t[node] = val
        return t[node]

    mid = (left + right) // 2
    left_val = update(t, idx, val, node * 2, left, mid)
    right_val = update(t, idx, val, node * 2 + 1, mid + 1, right)
    t[node] = left_val + right_val
    return t[node]


N, M, K = map(int, input().split())

numbers = [int(input()) for _ in range(N)]

tree = [0] * (N * 4)
build(numbers, tree, 1, 0, N - 1)

for _ in range(M + K):
    q, a, b = map(int, input().split())
    if q == 1:
        update(tree, a - 1, b, 1, 0, N - 1)
    else:
        print(query(tree, a - 1, b - 1, 1, 0, N - 1))
