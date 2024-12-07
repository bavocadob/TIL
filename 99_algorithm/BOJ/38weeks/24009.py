def power(base, exp, mod):
    result = 1
    while exp:
        if exp & 1:
            result = result * base % mod
        base = base * base % mod
        exp >>= 1
    return result


def solve(case, A, N, P):
    current = A % P
    for i in range(2, N + 1):
        current = power(current, i, P)
    print(f"Case #{case}: {current}")


T = int(input())
for t in range(1, T + 1):
    A, N, P = map(int, input().split())
    solve(t, A, N, P)
