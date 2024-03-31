def is_valid(target):
    additional = L

    cnt = 0

    for i in range(N):
        if A[i] >= target:
            cnt += 1
        elif A[i] + 1 >= target and additional > 0:
            cnt += 1
            additional -= 1
        else:
            break

    return cnt >= target


N, L = map(int, input().split())

A = list(map(int, input().split()))

A.sort(reverse=True)

left, right = 1, N

while left <= right:
    mid = (left + right) // 2

    if is_valid(mid):
        left = mid + 1
    else:
        right = mid - 1

print(left - 1)
