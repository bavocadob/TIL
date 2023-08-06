from math import sqrt


def get_gcd(num1, num2):
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp

    return num1


N = int(input())

numbers = [int(input()) for _ in range(N)]

numbers.sort()

result = numbers[1] - numbers[0]

for i in range(2, N):
    result = get_gcd(result, numbers[i] - numbers[i - 1])

answers = []

for i in range(1, int(sqrt(result)) + 1):
    if result % i == 0:
        answers.append(i)

M = len(answers)

for i in range(M - 1, -1, -1):
    if answers[i] ** 2 != result:
        answers.append(result // answers[i])

answers.pop(0)

print(*answers)
