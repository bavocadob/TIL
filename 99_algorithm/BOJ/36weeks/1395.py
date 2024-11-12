import sys

input = sys.stdin.readline


def lazy_update(node, start, end):
    if lazy[node]:
        tree[node] = (end - start + 1) - tree[node]
        if start != end:
            lazy[node * 2] = (lazy[node * 2] + 1) % 2
            lazy[node * 2 + 1] = (lazy[node * 2 + 1] + 1) % 2

    lazy[node] = 0


def update(start, end, left, right, node):
    lazy_update(node, left, right)

    if left > end or start > right:
        return

    if start <= left and right <= end:
        tree[node] = (right - left + 1) - tree[node]
        if left != right:
            lazy[node * 2] = (lazy[node * 2] + 1) % 2
            lazy[node * 2 + 1] = (lazy[node * 2 + 1] + 1) % 2
        return

    mid = (left + right) // 2
    update(start, end, left, mid, node * 2)
    update(start, end, mid + 1, right, node * 2 + 1)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]


def query(start, end, left, right, node):
    lazy_update(node, left, right)

    if left > end or start > right:
        return 0

    if start <= left and right <= end:
        return tree[node]

    mid = (left + right) // 2

    return query(start, end, left, mid, node * 2) + query(start, end, mid + 1, right, node * 2 + 1)


N, M = map(int, input().split())

lazy = [0] * (N * 4)
tree = [0] * (N * 4)

for _ in range(M):
    code, a, b = map(int, input().split())

    if code == 0:
        update(a - 1, b - 1, 0, N - 1, 1)
    else:
        print(query(a - 1, b - 1, 0, N - 1, 1))
