def solve():
    m = n - 1
    i = 1
    while True:
        b = 1 << ((i - 1) // 2)

        if m >= b:
            m -= b
        else:
            rst = m + (1 << ((i - 1) // 2))
            m //= (1 + (i % 2))

            for j in range(i % 2, (i - 1) // 2):
                rst = rst * 2 + m % 2
                m //= 2

            rst = rst if i == 1 else rst * 2 + 1
            return rst

        i += 1


n = int(input())

print(solve())
