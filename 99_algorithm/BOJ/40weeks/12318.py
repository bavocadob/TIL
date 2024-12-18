import sys

input = sys.stdin.readline
vowels = {"a", "e", "i", "o", "u"}


def solve(s, n):
    n_value = 0
    consecutive = 0
    last_pos = -1

    for i, char in enumerate(s):
        if char in vowels:
            consecutive = 0
        else:
            consecutive += 1

        if consecutive >= n:
            last_pos = i - n + 1

        if last_pos >= 0:
            n_value += last_pos + 1

    return n_value


T = int(input())
for ttt in range(1, T + 1):
    name, N = input().split()
    result = solve(name, int(N))
    print(f"Case #{ttt}: {result}")
