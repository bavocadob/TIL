import sys

input = sys.stdin.readline


def dfs(sharks, pos):
    if pos % 2 == 1:
        return 1

    size = len(sharks)
    max_eat = 0

    for target in range(pos + 1, size + 1):
        temp_sharks = sharks[:]
        new_sharks = []
        k = 0

        i = 0
        while i < len(temp_sharks):
            if i == pos:
                k = len(new_sharks)
                if target < size:
                    new_sharks.append(temp_sharks[i] + temp_sharks[target])
                    del temp_sharks[target]
                else:
                    new_sharks.append(temp_sharks[i])
                i -= 1
            else:
                if i + 1 < len(temp_sharks):
                    new_sharks.append(temp_sharks[i] + temp_sharks[i + 1])
                else:
                    new_sharks.append(temp_sharks[i])
            i += 2

        while k + 1 < len(new_sharks) and new_sharks[k] < new_sharks[k + 1]:
            new_sharks[k], new_sharks[k + 1] = new_sharks[k + 1], new_sharks[k]
            k += 1

        max_eat = max(max_eat, dfs(new_sharks, k))

    return max_eat + 1


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))

    print(f"Data Set {t}:")
    print(dfs(A, M - 1))
    print()
