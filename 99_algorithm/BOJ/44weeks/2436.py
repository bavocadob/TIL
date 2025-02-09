import sys

input = sys.stdin.readline


def check(a, b):
    return b if a % b == 0 else check(b, a % b)


gcd, lcm = map(int, input().split())
tmp = lcm // gcd

res_a, res_b = 0, 0
for i in range(1, int(tmp ** 0.5) + 1):
    if tmp % i == 0:
        left, right = i, tmp // i
        if check(left, right) == 1:
            res_a, res_b = left * gcd, right * gcd

print(res_a, res_b)
