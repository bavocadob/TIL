import math


def solve(n):
    if n > 0:
        for i in range(2, int(math.sqrt(n)) + 1):
            for j in range(32):
                tmp = i ** j
                if tmp > n:
                    break
                if tmp == n:
                    return j
    else:
        for i in range(-2, -int(math.sqrt(abs(n))) - 1, -1):
            for j in range(3, 32, 2):
                tmp = i ** j
                if tmp < n:
                    break
                if tmp == n:
                    return j

    return 1


while True:
    N = int(input())
    if N == 0:
        break
    print(solve(N))
