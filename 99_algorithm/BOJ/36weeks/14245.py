import sys

input = sys.stdin.readline


def build(left, right, node):
    if left == right:
        tree[node] = A[left]
        return tree[node]

    mid = (left + right) // 2

    tree[node] = build(left, mid, node * 2) ^ build(mid + 1, right, node * 2 + 1)
    return tree[node]


def lazy_update(left, right, node):
    if lazy[node]:
        if (right - left + 1) % 2:
            tree[node] ^= lazy[node]

        if left != right:
            lazy[node * 2] ^= lazy[node]
            lazy[node * 2 + 1] ^= lazy[node]

    lazy[node] = 0


def update(start, end, left, right, node, val):
    lazy_update(left, right, node)

    if left > end or right < start:
        return

    if start <= left and right <= end:
        if (right - left + 1) % 2:
            tree[node] ^= val

        if left != right:
            lazy[node * 2] ^= val
            lazy[node * 2 + 1] ^= val
        return

    mid = (left + right) // 2
    update(start, end, left, mid, node * 2, val)
    update(start, end, mid + 1, right, node * 2 + 1, val)

    tree[node] = tree[node * 2] ^ tree[node * 2 + 1]


def query(left, right, node, target):
    lazy_update(left, right, node)
    if left == right:
        return tree[node]

    mid = (left + right) // 2

    if left <= target <= mid:
        return query(left, mid, node * 2, target)
    else:
        return query(mid + 1, right, node * 2 + 1, target)


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
        idx = data[1]
        print(query(0, N - 1, 1, idx))
