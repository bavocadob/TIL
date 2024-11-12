import sys

input = sys.stdin.readline


def build(left, right, node):
    if left == right:
        tree[node] = A[left]
        return

    mid = (left + right) // 2

    build(left, mid, node * 2)
    build(mid + 1, right, node * 2 + 1)

    tree[node] = tree[node * 2] + tree[node * 2 + 1]


def update(start, end, val, left, right, node):
    if lazy[node]:
        tree[node] += (right - left + 1) * lazy[node]

        if left != right:
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]

        lazy[node] = 0

    if end < left or start > right:
        return

    if start <= left and right <= end:
        tree[node] += (right - left + 1) * val
        if left != right:
            lazy[node * 2] += val
            lazy[node * 2 + 1] += val

        return

    mid = (left + right) // 2
    update(start, end, val, left, mid, node * 2)
    update(start, end, val, mid + 1, right, node * 2 + 1)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]


def query(start, end, left, right, node):
    if lazy[node]:
        tree[node] += (right - left + 1) * lazy[node]

        if left != right:
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]

        lazy[node] = 0

    if end < left or start > right:
        return 0

    if start <= left and right <= end:
        return tree[node]

    mid = (left + right) // 2

    return query(start, end, left, mid, node * 2) + query(start, end, mid + 1, right, node * 2 + 1)


N, M, K = map(int, input().split())

A = [int(input()) for _ in range(N)]
tree = [0] * (N * 4)
lazy = [0] * (N * 4)

build(0, N - 1, 1)

for _ in range(M + K):
    data = list(map(int, input().split()))

    if data[0] == 1:
        l, r, v = data[1], data[2], data[3]
        update(l - 1, r - 1, v, 0, N - 1, 1)
    else:
        l, r = data[1], data[2]
        print(query(l - 1, r - 1, 0, N - 1, 1))
