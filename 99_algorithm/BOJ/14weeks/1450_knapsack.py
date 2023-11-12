from itertools import combinations


def get_subsum(arr):
    rst = []
    for i in range(len(arr) + 1):
        rst.extend([number for number in list(map(sum, combinations(arr, i))) if number <= C])
    return rst


N, C = map(int, input().split())

weights = list(map(int, input().split()))

arr_a = weights[:N // 2]
arr_b = weights[N // 2:]

subsum_a = get_subsum(arr_a)
subsum_b = get_subsum(arr_b)

del arr_a
del arr_b

subsum_b.sort()

ans = 0

for k in subsum_a:
    if k > C:
        continue
    left = 0
    right = len(subsum_b) - 1

    while left <= right:
        mid = (left + right) // 2

        if k + subsum_b[mid] <= C:
            left = mid + 1
        else:
            right = mid - 1
    ans += left

print(ans)
