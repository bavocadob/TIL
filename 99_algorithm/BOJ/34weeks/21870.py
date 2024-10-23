import math
from functools import reduce


def find_gcd_of_list(arr):
    return reduce(math.gcd, arr)


def solve(num_list, cnt):
    global ans

    if len(num_list) == 1:
        ans = max(ans, cnt + num_list[0])
        return

    l = len(num_list) // 2
    r = (len(num_list) + 1) // 2

    left = num_list[:l]
    right = num_list[-r:]


    solve(right, cnt + find_gcd_of_list(left))
    solve(left, cnt + find_gcd_of_list(right))


N = int(input())

ans = 0
nums = list(map(int, input().split()))
solve(nums, 0)
print(ans)