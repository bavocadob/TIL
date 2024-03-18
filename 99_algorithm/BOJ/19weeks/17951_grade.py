def solve(target):
    temp = 0
    cnt = 0

    for i in range(N):
        temp += A[i]

        if temp >= target:
            cnt += 1
            temp = 0

        if cnt == K:
            return True

    return False


N, K = map(int, input().split())

A = list(map(int, input().split()))

left = 0
right = sum(A)

while left <= right:
    mid = (left + right) // 2
    if solve(mid):
        left = mid + 1
    else:
        right = mid - 1

print(right)
