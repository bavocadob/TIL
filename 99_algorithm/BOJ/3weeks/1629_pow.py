# A의 B제곱을 C로 나눈 수
def solution(base, exponent, mod):
    result = 1
    temp = base
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * temp) % mod
        temp = (temp ** 2) % mod
        exponent //= 2

    return result


A, B, C = map(int, input().split())

print(solution(A, B, C))
