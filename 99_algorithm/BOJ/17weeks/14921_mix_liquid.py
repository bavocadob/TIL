N = int(input())

numbers = list(map(int, input().split()))

left = 0
right = N - 1

numbers.sort()
ans = numbers[left] + numbers[right]
while left < right:
    temp = numbers[left] + numbers[right]
    if temp > 0:
        right -= 1
    elif temp < 0:
        left += 1
    else:
        ans = 0
        break

    if abs(ans) > abs(temp):
        ans = temp

print(ans)
