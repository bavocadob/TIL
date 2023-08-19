def calc(formula):
    curr_value = 1
    curr_sum = 0
    curr_operator = '+'
    for i in range(N-1):
        if formula[i * 2 + 1] == ' ':
            curr_value = curr_value * 10 + (i + 2)
        else:
            if curr_operator == '+':
                curr_sum += curr_value
            elif curr_operator == '-':
                curr_sum -= curr_value

            curr_value = i + 2
            curr_operator = formula[i * 2 + 1]

    if curr_operator == '+':
        curr_sum += curr_value
    else:
        curr_sum -= curr_value

    return curr_sum


def solution(numbers, depth):
    if depth == N - 1:
        if calc(numbers) == 0:
            result.append(''.join(numbers))
        return

    # 만약 더하거나 빼는 경우 앞의 연산을 처리하고, 연산자를 변경한 후 밸류를 0으로 만들어 주고 넘김
    numbers[depth * 2 + 1] = '+'
    solution(numbers, depth + 1)
    numbers[depth * 2 + 1] = '-'
    solution(numbers, depth + 1)
    numbers[depth * 2 + 1] = ' '
    solution(numbers, depth + 1)

T = int(input())

for _ in range(T):
    N = int(input())

    arr = [' ' for _ in range(N * 2 - 1)]
    for i in range(N):
        arr[i * 2] = str(i + 1)

    result = []
    solution(arr, 0)
    result.sort()
    for line in result:
        print(line)
    print()
