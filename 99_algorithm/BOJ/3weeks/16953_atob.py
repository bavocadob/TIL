import sys


def solution(target, curr):
    if target == curr:
        return 1
    if curr % 2 == 0:
        return solution(target, curr // 2) + 1
    elif curr % 10 == 1 and (curr - 1) // 10 > target:
        return solution(target, (curr - 1) // 10) + 1


N, M = map(int, input().split())

try:
    print(solution(N, M))
except:
    print(-1)
