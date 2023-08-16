# import sys

# sys.setrecursionlimit(10000000)

mod = 1_000_000_007


# def solution(number):
#     # solution은 2의 number승을 10^ 9 + 7로 나눈 나머지를 반환하는 함수
#     # 이때 number // 2 * number // 2값과 같다.
#
#     if number == 1:
#         return 2
#
#     temp = solution(number // 2)
#     if number % 2:
#         return ((((temp % mod) ** 2) % mod) * 2) % mod
#     else:
#         return (temp * temp) % mod


def solution2(number):
    if number == 1:
        return 2

    result = 1
    temp = 2

    while number > 0:
        if number % 2 == 1:
            result = (result * temp) % mod
        temp = (temp ** 2) % mod
        number //= 2

    return result


N = int(input())

# print(solution(N - 1))
print(solution2(N - 1))
