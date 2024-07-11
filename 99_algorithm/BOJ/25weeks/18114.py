def binary_search(t, left, right):
    left += 1
    right -= 1

    while left <= right:
        mid = (left + right) // 2

        if A[mid] == t:
            return True
        elif A[mid] > t:
            right = mid - 1
        else:
            left = mid + 1

    return False


def solve():
    if C in A:
        return 1

    for i in range(N - 1):
        for j in range(i + 1, N):
            temp = A[i] + A[j]

            if temp == C:
                return 1
            elif temp > C:
                continue

            target = C - temp

            if binary_search(target, i, j):
                return 1
    return 0


N, C = map(int, input().split())

A = sorted(list(map(int, input().split())))

print(solve())
