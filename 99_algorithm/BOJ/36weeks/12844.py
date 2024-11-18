import sys

input = sys.stdin.readline


def build(left, right, node):
    if left == right:
        tree[node] = A[left]
        return
    mid = (left + right) // 2
    build(left, mid, node * 2)
    build(mid + 1, right, node * 2 + 1)
    tree[node] = tree[node * 2] ^ tree[node * 2 + 1]


def lazy_update(left, right, node):
    if lazy[node]:
        length = (right - left + 1)

        if (length % 2) == 1:
            tree[node] ^= lazy[node]

        if left != right:
            lazy[node * 2] ^= lazy[node]
            lazy[node * 2 + 1] ^= lazy[node]

    lazy[node] = 0


def update(start, end, left, right, node, val):
    lazy_update(left, right, node)
    if start > right or end < left:
        return

    if start <= left and right <= end:
        length = right - left + 1

        if length % 2 == 1:
            tree[node] ^= val

        if left != right:
            lazy[node * 2] ^= val
            lazy[node * 2 + 1] ^= val

        return

    mid = (left + right) // 2

    update(start, end, left, mid, node * 2, val)
    update(start, end, mid + 1, right, node * 2 + 1, val)
    tree[node] = tree[node * 2] ^ tree[node * 2 + 1]


def query(start, end, left, right, node):
    lazy_update(left, right, node)

    if start > right or end < left:
        return 0

    if start <= left and right <= end:
        return tree[node]

    mid = (left + right) // 2

    return query(start, end, left, mid, node * 2) ^ query(start, end, mid + 1, right, node * 2 + 1)


N = int(input())

A = list(map(int, input().split()))

tree = [0] * (N * 4)
lazy = [0] * (N * 4)

M = int(input())
build(0, N - 1, 1)
for _ in range(M):
    data = list(map(int, input().split()))

    if data[0] == 1:
        l, r, v = data[1], data[2], data[3]

        update(l, r, 0, N - 1, 1, v)
    else:
        l, r = data[1], data[2]
        print(query(l, r, 0, N - 1, 1))
