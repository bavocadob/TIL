def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def convert_to_fraction(integer_part, decimal_part):
    numerator = int(integer_part + decimal_part)
    denominator = 10 ** len(decimal_part)

    common_gcd = gcd(numerator, denominator)
    return numerator // common_gcd, denominator // common_gcd


def calculate_result(numerator, denominator):
    ans = [0] * 5
    diff = numerator - denominator

    for i in range(4, 0, -1):
        while diff >= i:
            ans[i] += 1
            diff -= i

    ans[0] = denominator - sum(ans)

    return ans


integer_part, decimal_part = input().split('.')
decimal_part = decimal_part.rstrip('0')

numerator, denominator = convert_to_fraction(integer_part, decimal_part)

result = calculate_result(numerator, denominator)

print(*result)
