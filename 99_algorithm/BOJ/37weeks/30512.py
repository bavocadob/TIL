import sys

input = sys.stdin.readline


def lazy_update(left, right, node):
    if lazy[node][0] != INF:
        tree[node] = min(tree[node], lazy[node][0])

        if left != right:
            if lazy[node * 2][0] > lazy[node][0]:
                lazy[node * 2] = lazy[node]

            if lazy[node * 2 + 1][0] > lazy[node][0]:
                lazy[node * 2 + 1] = lazy[node]
        else:
            if A[left] > lazy[node][0]:
                A[left] = lazy[node][0]
                prev[left] = lazy[node][1]
    lazy[node] = (INF, INF)


def build(left, right, node):
    if left == right:
        tree[node] = A[left]
        return

    mid = (left + right) // 2
    build(left, mid, node * 2)
    build(mid + 1, right, node * 2 + 1)

    tree[node] = min(tree[node * 2], tree[node * 2 + 1])


def update(start, end, left, right, node, val, seq):
    lazy_update(left, right, node)

    if left > end or start > right:
        return

    if start <= left and right <= end:
        tree[node] = min(tree[node], val)

        if left != right:
            if lazy[node * 2][0] > val:
                lazy[node * 2] = (val, seq)
            if lazy[node * 2 + 1][0] > val:
                lazy[node * 2 + 1] = (val, seq)
        else:
            if A[left] > val:
                A[left] = val
                prev[left] = seq
        return

    mid = (left + right) // 2
    update(start, end, left, mid, node * 2, val, seq)
    update(start, end, mid + 1, right, node * 2 + 1, val, seq)
    tree[node] = min(tree[node * 2], tree[node * 2 + 1])


def clean(left, right, node):
    lazy_update(left, right, node)
    if left != right:
        mid = (left + right) // 2
        clean(left, mid, node * 2)
        clean(mid + 1, right, node * 2 + 1)


INF = int(1e9)

N = int(input())

A = list(map(int, input().split()))
prev = [0] * N
Q = int(input())

tree = [0] * (N * 4)
lazy = [(INF, INF)] * (N * 4)

build(0, N - 1, 1)
for i in range(Q):
    a, b, c = map(int, input().split())
    update(a - 1, b - 1, 0, N - 1, 1, c, i)

clean(0, N - 1, 1)

rst = [0] * Q

for p in prev:
    rst[p] += 1

for i in range(1, Q):
    rst[i] += rst[i - 1]

print(*A)
print(*rst)
