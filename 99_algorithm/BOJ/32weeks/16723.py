N = int(input().strip())

result = 2 * N
N //= 2

i = 1
while True:
    result += (1 << i) * N
    N //= 2
    if N == 0:
        break
    i += 1

print(result)
