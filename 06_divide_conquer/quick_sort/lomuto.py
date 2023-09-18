nums = [43, 67, 13, 12 ,19, 68, 75,11, 46, 23, 51, 28, 34]


def quick_sort(arr, left, right):
    # 정복 대상의 범위를 가장 작아질 때 까지 계속 쪼갠다.
    if left < right:
        mid = cal(arr, left, right)
        quick_sort(arr, left, mid - 1)
        quick_sort(arr, mid + 1, right)


def cal(arr, left, right):
    # 피봇보다 큰 구간의 왼쪽 경계 = i
    i = left - 1
    # 피봇보다 큰 구간의 오른쪽 경계
    j = left
    pivot = arr[right]
    while j < right:
        if pivot > arr[j]:
            i += 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        j += 1

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    print(arr)
    return i + 1


quick_sort(nums, 0, len(nums) - 1)
print(nums)
