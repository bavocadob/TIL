def check(target):
    cnt = 1
    curr_min = curr_max = A[0]

    for i in range(1, N):
        if curr_min <= A[i] <= curr_max:
            continue
        else:
            if A[i] > curr_max:
                if A[i] - curr_min > target:
                    cnt += 1
                    curr_min = curr_max = A[i]
                else:
                    curr_max = A[i]
            else:
                if curr_max - A[i] > target:
                    cnt += 1
                    curr_min = curr_max = A[i]
                else:
                    curr_min = A[i]

        if cnt > M:
            return False

    return True


def solve():
    left = 0
    right = sum(A)

    ans = right

    while left <= right:
        mid = (left + right) // 2

        if check(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans


N, M = map(int, input().split())

A = list(map(int, input().split()))

print(solve())
