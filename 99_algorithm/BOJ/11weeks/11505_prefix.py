import sys

input = sys.stdin.readline

MOD = 1_000_000_007


def build(arr, t_arr, node, left, right):
    if left == right:
        t_arr[node] = arr[left]
        return t_arr[node]

    mid = (left + right) // 2

    left_val = build(arr, t_arr, node * 2, left, mid)
    right_val = build(arr, t_arr, node * 2 + 1, mid + 1, right)

    t_arr[node] = (left_val * right_val) % MOD
    return t_arr[node]


def update(t_arr, node, idx, val, left, right):
    if left == right:
        t_arr[node] = val
        return

    mid = (left + right) // 2

    if left <= idx <= mid:
        update(t_arr, node * 2, idx, val, left, mid)
    else:
        update(t_arr, node * 2 + 1, idx, val, mid + 1, right)

    t_arr[node] = (t_arr[node * 2] * t_arr[node * 2 + 1]) % MOD


def query(t_arr, node, start, end, left, right):
    if right < start or left > end:
        return 1

    if left >= start and right <= end:
        return t_arr[node] % MOD

    mid = (left + right) // 2
    left_val = query(t_arr, node * 2, start, end, left, mid)
    right_val = query(t_arr, node * 2 + 1, start, end, mid + 1, right)

    return (left_val * right_val) % MOD


method_dict = {1: update, 2: query}

N, M, K = map(int, input().split())

numbers = [0] + [int(input()) for _ in range(N)]

trees = [0] * (N * 4)

build(numbers, trees, 1, 0, N)

result = []

for _ in range(M + K):
    c, a, b = map(int, input().split())
    r = method_dict[c](trees, 1, a, b, 0, N)
    if r is not None:
        print(r)
