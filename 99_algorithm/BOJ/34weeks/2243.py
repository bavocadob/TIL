import sys

input = sys.stdin.readline


def update(t, idx, val, left, right, node):
    if left == right:
        t[node] = val
        return

    mid = (left + right) // 2

    if left <= idx <= mid:
        update(t, idx, val, left, mid, node * 2)
    else:
        update(t, idx, val, mid + 1, right, node * 2 + 1)

    t[node] = t[node * 2] + t[node * 2 + 1]


def query(t, left, right, node, acc, target):
    if left == right:
        return left

    l_val = t[node * 2]

    print(left, right, l_val, acc)
    mid = (left + right) // 2
    if acc + l_val >= target:
        return query(t, left, mid, node * 2, acc, target)
    else:
        return query(t, mid + 1, right, node * 2 + 1, acc + l_val, target)


N = int(input())

MAX_CANDY = 1_000_000
tree = [0] * (MAX_CANDY * 4)
size = [0] * (MAX_CANDY + 1)

for i in range(N):
    data = list(map(int, input().split()))
    print(f'{i}번째 상태 : {size[:5]}')

    if data[0] == 2:
        size[data[1]] += data[2]
        update(tree, data[1], size[data[1]], 1, MAX_CANDY, 1)
    else:
        rst = query(tree, 1, MAX_CANDY, 1, 0, data[1])
        print(rst)
        size[rst] -= 1
        update(tree, rst, size[rst], 1, MAX_CANDY, 1)
