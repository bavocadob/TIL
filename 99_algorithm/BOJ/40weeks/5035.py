import math


def solve():
    L, K, T1, T2, H = map(float, input().split())

    if K == 0:
        print(H, H)
        return

    a = K
    b = -K * (T1 + T2) - H
    c = L * T1
    T0 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    D = K * (T1 + T2 - T0)

    min_val = H + (0 if H <= L else D)
    max_val = H + (0 if H < L else D)

    print(min_val, max_val)


solve()
