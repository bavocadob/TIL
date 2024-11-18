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


def lazy_update(left, right, node):
    if lazy[node]:
        tree[node] += (right - left + 1) * lazy[node]

        if left != right:
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]

    lazy[node] = 0


def update(start, end, left, right, node, val):
    lazy_update(left, right, node)

    if left > end or right < start:
        return

    if start <= left and right <= end:
        tree[node] += (right - left + 1) * val
        if left != right:
            lazy[node * 2] += val
            lazy[node * 2 + 1] += val
        return

    mid = (left + right) // 2
    update(start, end, left, mid, node * 2, val)
    update(start, end, mid + 1, right, node * 2 + 1, val)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]


def query(start, end, left, right, node):
    lazy_update(left, right, node)

    if left > end or right < start:
        return 0

    if start <= left and right <= end:
        return tree[node]

    mid = (left + right) // 2
    return query(start, end, left, mid, node * 2) + query(start, end, mid + 1, right, node * 2 + 1)


N, M = map(int, input().split())

area_map = [0] * N

A = [0] * M

for i in range(M):
    a, b, c = map(int, input().split())
    for j in range(a - 1, b):
        area_map[j] = i

    A[i] = c

tree = [0] * (M * 4)
lazy = [0] * (M * 4)

build(0, M - 1, 1)

while True:
    data = tuple(map(int, input().split()))
    if data == (0, 0, 0):
        break

    if data[0] == 1:
        x, y = data[1] - 1, data[2] - 1
        ans = 0
        l, r = area_map[x], area_map[y]
        if x <= y:
            ans += query(l, r, 0, M - 1, 1)
        else:
            if l != r:
                ans += query(l, M - 1, 0, M - 1, 1)
                ans += query(0, r, 0, M - 1, 1)
            else:
                ans += query(0, M - 1, 0, M - 1, 1)
        print(ans)
    else:
        x, y, v = data[1] - 1, data[2] - 1, data[3]
        l, r = area_map[x], area_map[y]
        if x <= y:
            update(l, r, 0, M - 1, 1, v)
        else:
            if l != r:
                update(l, M - 1, 0, M - 1, 1, v)
                update(0, r, 0, M - 1, 1, v)
            else:
                update(0, M - 1, 0, M - 1, 1, v)
