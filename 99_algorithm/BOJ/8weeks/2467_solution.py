N = int(input())
numbers = list(map(int, input().split()))

numbers.sort()

l, r = numbers[0], numbers[-1]

left, right = 0, N - 1
gap = float('inf')

while left < right:
    temp = numbers[left] + numbers[right]
    if gap >= abs(temp):
        gap = abs(temp)
        l, r = numbers[left], numbers[right]

    if temp == 0:
        break
    elif temp > 0:
        right -= 1
    else:
        left += 1

print(l, r)
