import sys

input = sys.stdin.readline


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def solve():
    common_gcd = M[0]
    for i in range(1, m):
        common_gcd = gcd(common_gcd, M[i])

    common_lcm = 1
    for i in range(d):
        common_lcm = lcm(common_lcm, D[i])
        if common_lcm > common_gcd or common_lcm == 0:
            print(0)
            return

    count = 0
    i = 1
    while i * i < common_gcd:
        if common_gcd % i == 0:
            if i % common_lcm == 0:
                count += 1
            if (common_gcd // i) % common_lcm == 0:
                count += 1
        i += 1
    if i * i == common_gcd and (i % common_lcm == 0):
        count += 1

    print(count)


d, m = map(int, input().split())
D = list(map(int, input().split()))
M = list(map(int, input().split()))
solve()
