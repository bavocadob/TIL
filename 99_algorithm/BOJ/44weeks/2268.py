import sys

input = sys.stdin.readline


def update(idx, val, left, right, node):
    if left == right:
        tree[node] = val
        return

    mid = (left + right) // 2

    if left <= idx <= mid:
        update(idx, val, left, mid, node * 2)
    else:
        update(idx, val, mid + 1, right, node * 2 + 1)

    tree[node] = tree[node * 2] + tree[node * 2 + 1]


def query(start, end, left, right, node):
    if start > right or left > end:
        return 0

    if left >= start and right <= end:
        return tree[node]

    mid = (left + right) // 2

    return query(start, end, left, mid, node * 2) + query(start, end, mid + 1, right, node * 2 + 1)


N, M = map(int, input().split())

tree = [0] * (N * 4)

for _ in range(M):
    c, x, y = map(int, input().split())
    if c == 0:
        print(query(min(x, y) - 1, max(x, y) - 1, 0, N - 1, 1))
    else:
        update(x - 1, y, 0, N - 1, 1)
