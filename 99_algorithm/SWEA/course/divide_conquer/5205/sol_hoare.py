import sys

sys.stdin = open('input.txt')


# def hoare_partition(left, right):
#     pivot = arr[left]
#     i = left + 1
#     j = right
#
#     while True:
#
#         while i <= j and arr[i] <= pivot:
#             i += 1
#
#         while j >= i and arr[j] >= pivot:
#             j -= 1
#
#         print(i, j)
#         print(arr)
#         #
#         # print(f'left = {left} / right = {right} / arr = {arr}')
#
#         # 엇갈린 경우 right 가 pivot 의 위치
#         if i >= j:
#             return j
#
#         arr[i], arr[j] = arr[j], arr[i]
#
#
# def quick_sort(left, right):
#     # left 가 right 보다 커지면 종료
#     if left >= right:
#         return
#
#     pivot = hoare_partition(left, right)
#     arr[left], arr[pivot] = arr[pivot], arr[left]
#
#     quick_sort(left, pivot - 1)
#     quick_sort(pivot + 1, right)
#
#
# T = int(sys.stdin.readline())
# for tc input.txt range(1, T + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     quick_sort(0, len(arr) - 1)
#
#     print(f'{tc} {arr[N // 2]}')


########################################
def hoare_partition(left, right):
    pivot = arr[left]
    left += 1

    while True:
        while left <= right and arr[left] < pivot:
            left += 1
        while left <= right and arr[right] > pivot:
            right -= 1
        #
        # print(f'left = {left} / right = {right} / arr = {arr}')

        # 엇갈린 경우 right 가 pivot 의 위치
        if left >= right:
            return right

        arr[left], arr[right] = arr[right], arr[left]


def quick_sort(left, right):
    # left 가 right 보다 커지면 종료
    if left >= right:
        return

    pivot = hoare_partition(left, right)
    arr[left], arr[pivot] = arr[pivot], arr[left]

    quick_sort(left, pivot)
    quick_sort(pivot + 1, right)


T = int(sys.stdin.readline())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(0, len(arr) - 1)
    print(arr)
    print(f'{tc} {arr[N // 2]}')
