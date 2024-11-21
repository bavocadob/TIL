def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


N = int(input())

digits = list({int(d) for d in str(N) if d != '0'})

current_lcm = digits[0]
for digit in digits[1:]:
    current_lcm = lcm(current_lcm, digit)

if N % current_lcm == 0:
    print(N)
else:
    cnt = 1
    while True:
        for i in range(10 ** cnt):
            suffix = str(i).zfill(cnt)
            candidate = int(str(N) + suffix)
            if candidate % current_lcm == 0:
                print(candidate)
                exit()
        cnt += 1
