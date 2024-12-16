MOD = 1_000_000_007


def modulo(a, b):
    result = 1
    a %= MOD
    while b > 0:
        if b & 1:
            result = (result * a) % MOD
        a = (a * a) % MOD
        b >>= 1
    return result


A, B, N = map(int, input().split())
print(modulo(modulo(2, 31), N - 1))
