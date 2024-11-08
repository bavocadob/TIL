import sys

input = sys.stdin.readline


def build(start, end, node):
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = build(start, mid, node * 2) + build(mid + 1, end, node * 2 + 1)
    return tree[node]


def update_range(start, end, node, left, right, value):
    # lazy 값이 있으면 먼저 현재 노드에 적용
    if lazy[node] != 0:
        tree[node] += (end - start + 1) * lazy[node]
        if start != end:
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]
        lazy[node] = 0  # 현재 노드의 lazy 초기화

    # 현재 구간이 업데이트 구간에서 벗어난 경우
    if end < left or start > right:
        return

    # 업데이트 구간이 현재 구간을 완전히 포함하는 경우
    if left <= start and end <= right:
        tree[node] += (end - start + 1) * value
        if start != end:  # 리프 노드가 아니면 자식에게 lazy 값을 전파
            lazy[node * 2] += value
            lazy[node * 2 + 1] += value
        return

    mid = (start + end) // 2
    update_range(start, mid, node * 2, left, right, value)
    update_range(mid + 1, end, node * 2 + 1, left, right, value)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]


def query_index(start, end, node, index):
    # lazy 값이 있으면 먼저 현재 노드에 적용
    if lazy[node] != 0:
        tree[node] += (end - start + 1) * lazy[node]
        if start != end:
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]
        lazy[node] = 0  # 현재 노드의 lazy 초기화

    if start == end:
        return tree[node]

    mid = (start + end) // 2
    if index <= mid:
        return query_index(start, mid, node * 2, index)
    else:
        return query_index(mid + 1, end, node * 2 + 1, index)


N = int(input())
nums = list(map(int, input().split()))
M = int(input())

lazy = [0] * (N * 4)
tree = [0] * (N * 4)

build(0, N - 1, 1)

for _ in range(M):
    data = list(map(int, input().split()))
    if data[0] == 1:
        i, j, k = data[1] - 1, data[2] - 1, data[3]
        update_range(0, N - 1, 1, i, j, k)
    else:
        target_idx = data[1] - 1
        print(query_index(0, N - 1, 1, target_idx))
