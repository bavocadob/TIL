
def solve(x, y):
    integer_part = x // y
    remainder = x % y

    if remainder == 0:
        return f"{integer_part}.(0)"

    # 소수부 계산
    seen_remainders = {}
    decimal_part = []
    idx = 0

    while remainder != 0:
        # 순환 발견
        if remainder in seen_remainders:
            start_idx = seen_remainders[remainder]
            non_repeating = ''.join(decimal_part[:start_idx])
            repeating = ''.join(decimal_part[start_idx:])
            return f"{integer_part}.{non_repeating}({repeating})"

        # 나머지 기록
        seen_remainders[remainder] = idx
        idx += 1

        # 나머지를 이용해 소수부 계산
        remainder *= 10
        decimal_part.append(str(remainder // y))
        remainder %= y

    # 순환이 없을 경우
    non_repeating = ''.join(decimal_part)
    return f"{integer_part}.{non_repeating}(0)"


N = int(input())

for _ in range(N):
    x, y = map(int, input().split())
    print(solve(x, y))
