N, X = map(int, input().split())

A = list(map(int, input().split()))
A.sort()
ans = 0

while A and A[-1] == X:
    ans += 1
    A.pop()

rest = 0

left = 0
right = len(A) - 1

while left < right:

    if (A[left] + A[right]) * 2 >= X:
        ans += 1
        left += 1
        right -= 1
    else:
        left += 1
        rest += 1

if left == right:
    rest += 1

print(ans + (rest // 3))
