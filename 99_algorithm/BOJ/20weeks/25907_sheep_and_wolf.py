import sys


def solve():
    l, r = 1, N
    while l + 1 < r:
        m = (l + r) // 2

        sys.stdout.write(f'? {m}\n')
        sys.stdout.flush()
        temp = int(sys.stdin.readline())

        if m % 2 == 0 and m // 2 == temp:
            sys.stdout.write(f'! {m}')
            sys.stdout.flush()
            return

        if m // 2 < temp:
            l = m
        else:
            r = m

    sys.stdout.write(f'! {l}')
    sys.stdout.flush()


N = int(input())

solve()
