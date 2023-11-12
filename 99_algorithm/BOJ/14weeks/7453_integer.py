import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


def upper_bound(arr, target):
    l, r = 0, len(arr)

    while l < r:
        mid = l + (r - l) // 2
        if arr[mid] <= target:
            l = mid + 1
        else:
            r = mid
    return left


def lower_bound(arr, target):
    l, r = 0, len(arr)
    while l < r:
        mid = l + (r - l) // 2
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid

    return l


N = int(input())

A = []
B = []
C = []
D = []

for _ in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

case_a = []
case_b = []

for i in range(N):
    for j in range(N):
        case_a.append(A[i] + B[j])
        case_b.append(C[i] + D[j])

case_a.sort()
case_b.sort()

left = 0
right = len(case_b) - 1
ans = 0

while right >= 0 and left < len(case_a):
    temp = case_a[left] + case_b[right]
    if temp > 0:
        right -= 1
    elif temp < 0:
        left += 1
    else:
        # ab_right = upper_bound(case_a, case_a[left])
        # cd_left = lower_bound(case_b, case_b[right])
        ab_right = bisect_right(case_a, case_a[left])
        cd_left = bisect_left(case_b, case_b[right]) - 1

        ans += (ab_right - left) * (right - cd_left)

        left = ab_right
        right = cd_left

print(ans)
