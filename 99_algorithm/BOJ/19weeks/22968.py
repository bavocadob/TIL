import sys

input = sys.stdin.readline

rst = []

for _ in range(int(input())):
    V = int(input())

    a = 4
    b = 2
    c = 3

    if 3 > V:
        rst.append(V)
        continue

    curr = 7

    while V >= curr:
        b = a
        a = curr
        c += 1
        curr = a + b + 1

    rst.append(c)

for ans in rst:
    print(ans)
