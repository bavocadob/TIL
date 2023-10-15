def update(arr, node, idx, val, left, right):
    if idx < left or idx > right:
        return

    arr[node] += val

    if left != right:
        mid = (left + right) // 2
        update(arr, node * 2, idx, val, left, mid)
        update(arr, node * 2 + 1, idx, val, mid + 1, right)


    # if left <= idx <= mid:
    #     update(arr, node * 2, idx, val, left, mid)
    # else:
    #     update(arr, node * 2 + 1, idx, val, mid + 1, right)
    #
    # arr[node] = arr[node * 2] + arr[node * 2 + 1]


def query(arr, node, start, end, left, right):
    if left > end or right < start:
        return 0

    if left >= start and right <= end:
        return arr[node]

    mid = (left + right) // 2
    left_val = query(arr, node * 2, start, end, left, mid)
    right_val = query(arr, node * 2 + 1, start, end, mid + 1, right)

    return left_val + right_val


N = int(input())

a_line = list(map(int, input().split()))

b_line = list(map(int, input().split()))
b_line_dict = {b_line[i]: i for i in range(N)}

trees = [0] * (N * 4)

ans = 0

for code in a_line:
    b_idx = b_line_dict[code]
    update(trees, 1, b_idx, 1, 0, N - 1)
    if b_idx == N - 1:
        continue

    ans += query(trees, 1, b_idx + 1, N - 1, 0, N - 1)
print(ans)
