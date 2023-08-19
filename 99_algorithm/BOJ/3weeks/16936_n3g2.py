from collections import deque

N = int(input())

numbers = set(map(int, input().split()))

result = deque([numbers.pop()])

while result[-1] * 2 in numbers or (result[-1] % 3 == 0 and result[-1] // 3 in numbers):
    if result[-1] * 2 in numbers:
        numbers.remove(result[-1] * 2)
        result.append(result[-1] * 2)
    elif result[-1] % 3 == 0 and result[-1] // 3 in numbers:
        numbers.remove(result[-1] // 3)
        result.append(result[-1] // 3)

while result[0] // 2 in numbers or (result[0] * 3 in numbers):
    if result[0] // 2 in numbers:
        numbers.remove(result[0] // 2)
        result.appendleft(result[0] // 2)
    elif result[0] * 3 in numbers:
        numbers.remove(result[0] * 3)
        result.appendleft(result[0] * 3)

print(*list(result))
