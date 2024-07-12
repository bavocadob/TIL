import bisect


def count_occurrences_in_range(arr, target, start, end):
    left_index = bisect.bisect_left(arr, target, start, end + 1)
    right_index = bisect.bisect_right(arr, target, start, end + 1)

    if left_index == len(arr) or arr[left_index] != target:
        return 0

    return right_index - left_index

def check_one():
    global ans

    target = A[-1]
    need = sum(A[:-1]) - target

    if need <= 0:
        return

    for i in range(N - 2):
        first = A[i]

        second = need - first

        if second <= 0:
            continue

        ans += count_occurrences_in_range(A, second, i + 1, N - 2)


def check_two():
    global ans
    target = A[-2]
    temp = sum(A[:-2])

    if temp > target:
        need = temp - target
        ans += count_occurrences_in_range(A, need, 0, N - 3)


def check_three():
    global ans

    if A[-3] == sum(A[:-3]):
        ans += 1


N = int(input())

A = list(map(int, input().split()))
A.sort()
ans = 0

check_one()
check_two()
check_three()
print(ans)
