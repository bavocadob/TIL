def f(x):
    return (x << 1) ^ 6 if x & 1 else (x >> 1) ^ 6


def main():
    a, n = map(int, input().split())
    seen = set()
    sequence = []

    while n > 0:
        a = f(a)
        if a in seen:
            break
        seen.add(a)
        n -= 1

    if n <= 0:
        print(a)
        return

    sequence.append(a)
    j = f(a)
    length = 1
    # print(a)

    while j != a:
        sequence.append(j)
        j = f(j)
        length += 1

    print(sequence[(n + length - 1) % length])


if __name__ == "__main__":
    main()
