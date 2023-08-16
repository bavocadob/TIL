import sys

sys.stdin = open('input.txt')
sys.setrecursionlimit(1000000)


def rsp(a, b):
    if cards[a - 1] == cards[b - 1]:
        return a

    if cards[a - 1] == 1 and cards[b - 1] == 2:
        return b
    elif cards[a - 1] == 1 and cards[b - 1] == 3:
        return a
    elif cards[a - 1] == 2 and cards[b - 1] == 1:
        return a
    elif cards[a - 1] == 2 and cards[b - 1] == 3:
        return b
    elif cards[a - 1] == 3 and cards[b - 1] == 1:
        return b
    elif cards[a - 1] == 3 and cards[b - 1] == 2:
        return a


def solution(left, right):

    if right == left:
        return left

    mid = (left + right) // 2
    # 0 ~ 3
    # 0 ~ 1, 2 ~ 3
    l = solution(left, mid)
    r = solution(mid + 1, right)

    return rsp(l, r)


T = int(input())

for tc in range(T):
    N = int(input())
    cards = list(map(int, input().split()))

    print(f'#{tc+1} {solution(1, N)}')
