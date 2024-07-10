def solve():
    left = 0
    right = N

    while left <= right:
        mid = (left + right) // 2

        x = mid + 1
        y = N - mid + 1
        temp = x * y

        if temp == K:
            print('YES')
            return
        elif temp > K:
            right = mid - 1
        else:
            left = mid + 1

    print('NO')


N, K = map(int, input().split())

solve()
