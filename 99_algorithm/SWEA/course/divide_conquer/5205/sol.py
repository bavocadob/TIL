import sys

sys.stdin = open('input.txt')


def quick_sort(arr, left, right):
    if left < right:
        s = partition(arr, left, right)

        quick_sort(arr, left, s - 1)
        quick_sort(arr, s + 1, right)


def partition(arr, left, right):
    pivot = arr[left]
    i = left
    j = right

    while i <= j:
        while i <= j and arr[i] <= pivot:
            # print(i)
            i += 1
        while i <= j and arr[j] >= pivot:
            # print(j)
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]
    # print(arr)
    # print(j)
    return j


T = int(input())

for tc in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    quick_sort(numbers, 0, N - 1)
    # print(numbers)
    print(f'#{tc+1} {numbers[N // 2]}')
