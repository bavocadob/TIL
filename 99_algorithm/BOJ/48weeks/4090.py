import bisect
import sys

input = sys.stdin.readline


def check(x):
    s = sorted(str(x))

    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            compare = sorted(str(i) + str(x // i))
            if compare == s:
                return True
    return False


v_numbers = [num for num in range(1, 1_000_256) if check(num)]

while True:
    n = int(input())
    if n == 0:
        break

    idx = bisect.bisect_left(v_numbers, n)
    print(v_numbers[idx])
