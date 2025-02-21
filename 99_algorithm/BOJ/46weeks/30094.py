import math
import sys
from collections import defaultdict
from typing import Callable

input = sys.stdin.readline
MOD = 998_244_353


def solve(arr: list, key: Callable[[tuple], int]):
    arr.sort(key=key)

    cnt = defaultdict(int)
    rst = []
    ans = 0
    for i in range(N):
        ci, ai, idx = arr[i]

        ans += ci * i + ai * (N - 1 - i)
        rst.append(idx)
        cnt[ci - ai] += 1

    case = 1
    for key, val in cnt.items():
        case *= math.factorial(val)
        case %= MOD
    print(ans, case)
    print(*rst)


N = int(input())

A = [(*map(int, input().split()), i + 1) for i in range(N)]

solve(A, key=lambda x: x[1] - x[0])
solve(A, key=lambda x: x[0] - x[1])
