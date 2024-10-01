import sys

from collections import deque

input = sys.stdin.readline


def build(left, right, node):
    if left == right:
        tree[node] = A[left]
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


def query(left, right, node, curr):
    if left == right:
        return left

    mid = (left + right) // 2
    l_val = tree[node * 2]

    if curr + l_val >= mid_idx:
        return query(left, mid, node * 2, curr)
    else:
        return query(mid + 1, right, node * 2 + 1, curr + l_val)


N, K = map(int, input().split())
mid_idx = (K + 1) // 2
A = [0] * 65536

tree = [0] * (65536 * 4)

q = deque()
for _ in range(K):
    num = int(input())

    A[num] += 1
    q.append(num)

build(0, 65535, 1)
ans = query(0, 65535, 1, 0)

for _ in range(N - K):
    temp = q.popleft()
    A[temp] -= 1
    update(temp, A[temp], 0, 65535, 1)

    temp = int(input())
    A[temp] += 1
    q.append(temp)
    update(temp, A[temp], 0, 65535, 1)

    ans += query(0, 65535, 1, 0)

print(ans)
