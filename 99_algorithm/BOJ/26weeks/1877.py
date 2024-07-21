def prime_factors(N):
    factors = []
    while N % 2 == 0:
        factors.append(2)
        N = N // 2

    for i in range(3, int(N ** 0.5) + 1, 2):
        while N % i == 0:
            factors.append(i)
            N = N // i

    if N > 2:
        factors.append(N)

    return factors


M = int(input())

rst = []

if 3 >= M:
    rst += [1, 1]
else:
    temp = M // 3
    mod = M % 3

    if mod == 0:
        rst.append(temp)
    else:
        rst.append(temp + 1)

    if mod <= 1:
        rst.append(temp)
    else:
        rst.append(temp + 1)

if M == 1:
    rst += [1, 1]
else:
    M_factors = prime_factors(M)

    rst.append(len(M_factors))

    two_cnt = M_factors.count(2)
    rst.append(len(M_factors) - two_cnt // 2)

print(*rst)
