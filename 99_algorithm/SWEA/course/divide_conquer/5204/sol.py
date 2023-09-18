import sys

sys.stdin = open('input.txt')


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)

    return merge(left_arr, right_arr)


def merge(left_arr, right_arr):
    global ans

    if left_arr[-1] > right_arr[-1]:
        ans += 1
    new_arr = []

    left = 0
    right = 0
    while left < len(left_arr) and right < len(right_arr):
        if left_arr[left] >= right_arr[right]:
            new_arr.append(right_arr[right])
            right += 1
        else:
            new_arr.append(left_arr[left])
            left += 1

    if left == len(left_arr):
        while right < len(right_arr):
            new_arr.append(right_arr[right])
            right += 1
    else:
        while left < len(left_arr):
            new_arr.append(left_arr[left])
            left += 1

    return new_arr


T = int(input())

for tc in range(T):
    N = int(input())

    numbers = list(map(int, input().split()))

    ans = 0
    sorted_arr = merge_sort(numbers)
    # print(sorted_arr)
    print(f'#{tc + 1} {sorted_arr[N // 2]} {ans}')
