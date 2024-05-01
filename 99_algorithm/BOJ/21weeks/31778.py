def solve():
    N, K = map(int, input().split())

    if N < 3:
        return 0

    left = 0
    right = N - 1

    S = list(input().rstrip())
    for _ in range(K):
        while left < right and S[left] == 'P':
            left += 1

        while left < right and S[right] == 'C':
            right -= 1

        if left < right and S[left] == 'C' and S[right] == 'P':
            S[left], S[right] = S[right], S[left]
            left += 1
            right -= 1
        else:
            break

    try:
        idx = S.index('P', 1) + 1
    except ValueError:
        return 0

    cnt = 2
    x = 1
    ans = 0

    while idx < N:
        if S[idx] == 'C':
            ans += x
        else:
            cnt += 1
            x *= cnt
            x //= cnt - 2

        idx += 1

    return ans


print(solve())
