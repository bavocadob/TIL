import sys

input = sys.stdin.readline


def build(left, right, node):
    if left == right:
        tree[node] = cnt[left]
        return

    mid = (left + right) // 2
    build(left, mid, node * 2)
    build(mid + 1, right, node * 2 + 1)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]


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


def query(left, right, node, s):
    if left == right:
        return left

    mid = (left + right) // 2
    left_sum = tree[node * 2]

    if left_sum + s == (M * 2 - 1):
        return query(left, mid, node * 2, s)
    else:
        return query(mid + 1, right, node * 2 + 1, s + left_sum)


N, M = map(int, input().split())

nums = list(map(int, input().split()))

size = 1_000_001
cnt = [0] * size
tree = [0] * (size * 4)

for i in range(M * 2 - 1):
    cnt[nums[i]] += 1

build(0, size - 1, 1)
print(query(0, size - 1, 1, 0), end=' ')

for i in range(N - (M * 2 - 1)):
    l_del = nums[i]
    r_plus = nums[i + (M * 2 - 1)]
    cnt[l_del] -= 1
    cnt[r_plus] += 1
    if l_del == r_plus:
        update(l_del, cnt[l_del], 0, size - 1, 1)
    else:
        update(l_del, cnt[l_del], 0, size - 1, 1)
        update(r_plus, cnt[r_plus], 0, size - 1, 1)

    print(query(0, size - 1, 1, 0), end=' ')
