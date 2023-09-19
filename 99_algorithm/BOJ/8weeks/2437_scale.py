N = int(input())

numbers = list(map(int, input().split()))

target = 1
numbers.sort()
while numbers:
    print(numbers, target)
    if target in numbers:
        numbers.remove(target)
        target += target
    else:
        for i in range(len(numbers), -1, -1):
            if numbers[i] < target:
                n = numbers.pop(i)
                target += n
        else:
            numbers.clear()

print(target)


