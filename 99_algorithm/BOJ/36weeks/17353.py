import sys

input = sys.stdin.readline


def lazy_update(left, right, node):
    if lazy[node]:
        tree[node] += (right - left + 1) * lazy[node]

        if left != right:
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]
    lazy[node] = 0


def build(left, right, node):
    if left == right:
        tree[node] = B[left]
        return

    mid = (left + right) // 2

    build(left, mid, node * 2)
    build(mid + 1, right, node * 2 + 1)

    tree[node] = tree[node * 2] + tree[node * 2 + 1]


def update(start, end, left, right, node, val):
    lazy_update(left, right, node)

    if left > end or right < start:
        return

    mid = (left + right) // 2

    if start <= left and right <= end:
        tree[node] += (right - left + 1) * val

        if left != right:
            lazy[node * 2] += val
            lazy[node * 2 + 1] += val
        return

    update(start, end, left, mid, node * 2, val)
    update(start, end, mid + 1, right, node * 2 + 1, val)

    tree[node] = tree[node * 2] + tree[node * 2 + 1]


def query(start, end, left, right, node):
    lazy_update(left, right, node)

    if start > right or left > end:
        return 0

    if start <= left and right <= end:
        return tree[node]

    mid = (left + right) // 2
    return query(start, end, left, mid, node * 2) + query(start, end, mid + 1, right, node * 2 + 1)


N = int(input())

A = list(map(int, input().split()))
B = [A[0]]

for i in range(1, N):
    B.append(A[i] - A[i - 1])
tree = [0] * (N * 4)
lazy = [0] * (N * 4)
M = int(input())

build(0, N - 1, 1)

for _ in range(M):
    data = list(map(int, input().split()))
    if data[0] == 1:
        l, r = data[1], data[2]
        update(l - 1, r - 1, 0, N - 1, 1, 1)
        update(r, r, 0, N - 1, 1, -(r - l + 1))
    else:
        t = data[1]
        print(query(0, t - 1, 0, N - 1, 1))
