import sys

sys.stdin = open('input.txt')

import itertools


def solution(original_arr, sum_arr):
    for i in range(N - 1, -1, -1):
        for j in range(i + 1):
            if original_arr[i] - original_arr[j] in sum_arr:
                return original_arr[i]


N = int(input())

numbers = [int(input()) for _ in range(N)]
numbers.sort()
sum_lst = set(map(sum, list(itertools.combinations_with_replacement(numbers, 2))))
print(solution(numbers, sum_lst))
