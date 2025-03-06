N = int(input())
for length in range(2, int((2 * N) ** 0.5) + 1):
    remainder = N - (length * (length - 1) // 2)
    if remainder % length == 0:
        start = remainder // length
        print(start, start + length - 1)
