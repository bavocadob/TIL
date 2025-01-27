import math

n = int(input())

p = [0.0] * 141
c = [[0.0] * 141 for _ in range(141)]

for i in range(n + 1):
    c[i][0] = 1
    for j in range(1, i + 1):
        c[i][j] = c[i - 1][j] + c[i - 1][j - 1]

    p[i] = math.pow(i - 1, i)
    for j in range(2, i - 1):
        p[i] -= math.pow(i - j - 1, i - j) * c[i - 1][j - 1] * p[j]

result = p[n] / math.pow(n - 1, n)
print(f"{result:.9f}")
