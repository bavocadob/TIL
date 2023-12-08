N, K, T = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort()

left = 0
right = N - 1

while left < right and T >= 0:
    move = min(K - numbers[right], numbers[left])

    numbers[left] -= move
    numbers[right] += move
    T -= move

    if numbers[left] == 0:
        left += 1
        N -= 1

    if numbers[right] == K:
        right -= 1
        N -= 1

if (N == 0 and T >= 0) or sum(numbers) == 0:
    print('YES')
else:
    print('NO')
