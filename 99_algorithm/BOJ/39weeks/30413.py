MOD = 1_000_000_007


def pw(val, sq):
    if sq == 1:
        return val % MOD
    ret = pw(val, sq // 2)
    ret = ret * ret % MOD
    if sq % 2 != 0:
        ret = ret * val % MOD
    return ret


a, b = map(int, input().split())
if a == 1:
    print(b % MOD)
else:
    numerator = (pw(a, b) - 1 + MOD) % MOD

    denominator = pw(a - 1, MOD - 2)
    print(numerator * denominator % MOD)
