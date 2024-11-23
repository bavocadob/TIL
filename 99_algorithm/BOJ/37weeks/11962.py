import sys
from typing import List, Callable

input = sys.stdin.readline


def build(
        tree: List[int],
        left: int,
        right: int,
        node: int,
        execute: Callable[[List[int], int, int], int]
) -> None:
    if left == right:
        tree[node] = A[left]
        return

    mid = (left + right) // 2
    build(tree, left, mid, node * 2, execute)
    build(tree, mid + 1, right, node * 2 + 1, execute)

    tree[node] = execute(tree, node * 2, node * 2 + 1)


def lazy_update(
        left: int,
        right: int,
        node: int,
) -> None:
    if lazy[node] != 0:
        tree_sum[node] += (right - left + 1) * lazy[node]
        tree_min[node] += lazy[node]

        if left != right:
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]

        lazy[node] = 0


def update(start, end, left, right, node, val):
    lazy_update(left, right, node)

    if left > end or start > right:
        return

    if start <= left and right <= end:
        tree_sum[node] += (right - left + 1) * val
        tree_min[node] += val

        if left != right:
            lazy[node * 2] += val
            lazy[node * 2 + 1] += val
        return

    mid = (left + right) // 2
    update(start, end, left, mid, node * 2, val)
    update(start, end, mid + 1, right, node * 2 + 1, val)

    tree_sum[node] = execute_sum(tree_sum, node * 2, node * 2 + 1)
    tree_min[node] = execute_min(tree_min, node * 2, node * 2 + 1)


def query(tree, start, end, left, right, node, check, base):
    lazy_update(left, right, node)

    if left > end or start > right:
        return base

    if start <= left and right <= end:
        return tree[node]

    mid = (left + right) // 2
    return check(query(tree, start, end, left, mid, node * 2, check, base),
                 query(tree, start, end, mid + 1, right, node * 2 + 1, check, base))


def execute_sum(tree: List[int], left_node: int, right_node: int) -> int:
    return tree[left_node] + tree[right_node]


def execute_min(tree: List[int], left_node: int, right_node: int) -> int:
    return min(tree[left_node], tree[right_node])


N, Q = map(int, input().split())
A = list(map(int, input().split()))

tree_sum = [0] * (N * 4)
tree_min = [0] * (N * 4)
lazy = [0] * (N * 4)
build(tree_sum, 0, N - 1, 1, execute_sum)
build(tree_min, 0, N - 1, 1, execute_min)

for _ in range(Q):
    code, *data = input().rstrip().split()

    if code == 'P':
        l, r, v = map(int, data)
        update(l - 1, r - 1, 0, N - 1, 1, v)
    else:
        l, r = map(int, data)
        if code == 'S':
            print(query(tree_sum, l - 1, r - 1, 0, N - 1, 1, lambda x, y: x + y, 0))
        else:
            print(query(tree_min, l - 1, r - 1, 0, N - 1, 1, min, int(1e9)))
