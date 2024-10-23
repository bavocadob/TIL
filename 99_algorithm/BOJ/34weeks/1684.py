import math
from functools import reduce


def find_gcd_of_list(arr):
    return reduce(math.gcd, arr)


N = int(input())


gap = []

nums = list(map(int, input().split()))

for i in range(N - 1):
    gap.append(abs(nums[i] - nums[i + 1]))

print(find_gcd_of_list(gap))