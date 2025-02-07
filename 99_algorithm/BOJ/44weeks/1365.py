def binary_search(target):
    left = 0
    right = len(B) - 1

    while left <= right:

        mid = (left + right) // 2

        if B[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


N = int(input())

A = list(map(int, input().split()))

B = [A[0]]

for i in range(1, N):
    num = A[i]

    pos = binary_search(num)

    if pos == len(B):
        B.append(num)
    elif B[pos] > num:
        B[pos] = num

print(N - len(B))
