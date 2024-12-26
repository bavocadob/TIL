import math


N = int(input())
result_set = set()

for i in range(1, int(math.sqrt(N)) + 1):
    if (N - i * i) % (2 * i) == 0:
        x = ((N - i * i) // (2 * i)) ** 2
        if x != 0 and (x + N) != 0:
            result_set.add(x)

    if (N + i * i) % (2 * i) == 0:
        x = ((N + i * i) // (2 * i)) ** 2
        if x != 0 and (N - x) != 0:
            result_set.add(-x)

    x = N - i * i
    y = int(math.sqrt(x + 0.5))
    if y * y == x and y != 0:
        result_set.add(-(i * i))


result_list = sorted(result_set)
print(len(result_list))
if result_list:
    print(" ".join(map(str, result_list)))
