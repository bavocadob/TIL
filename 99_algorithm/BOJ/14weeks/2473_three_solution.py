def solution():
    ans = float('inf')

    rst = [0, 0, 0]

    for i in range(N - 2):
        left = i + 1
        right = N - 1
        while left < right:
            temp = A[i] + A[left] + A[right]
            if abs(temp) < ans:
                ans = abs(temp)
                rst[0] = A[i]
                rst[1] = A[left]
                rst[2] = A[right]

            if temp > 0:
                right -= 1
            elif temp < 0:
                left += 1
            else:
                return rst
    return rst


N = int(input())

A = list(map(int, input().split()))
A.sort()

print(*solution())
