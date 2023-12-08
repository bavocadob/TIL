import sys

input = sys.stdin.readline


def calc(number, base):
    rst = 0
    temp_base = 1
    while number:
        rst += (number % 10) * temp_base
        number //= 10
        temp_base *= base

    return rst


def solution():
    x, y = map(int, input().split())

    left = 10
    right = 10

    while True:
        cal_x = calc(x, left)
        cal_y = calc(y, right)
        if cal_y > cal_x:
            left += 1
        elif cal_x > cal_y:
            right += 1
        else:  # 찾은 경우
            print(left, right)
            break


T = int(input())

for tc in range(T):
    solution()
