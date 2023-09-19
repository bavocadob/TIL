N = int(input())

numbers = list(map(int, input().split()))
target = 1
numbers.sort()
while numbers:

    for i in range(len(numbers) - 1, -1, -1):
        if numbers[i] <= target:
            target += numbers.pop(i)
            break
    else:
        numbers.clear()
print(target)
