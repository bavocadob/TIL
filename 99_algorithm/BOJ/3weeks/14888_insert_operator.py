min_val = int(1e9)
max_val = -min_val


def solution(depth, oper_arr, num_arr, value):
    global min_val, max_val
    if depth == N:
        min_val = min(min_val, value)
        max_val = max(max_val, value)
        return

    if oper_arr[0] > 0:
        oper_arr[0] -= 1
        solution(depth + 1, oper_arr, num_arr, value + num_arr[depth])
        oper_arr[0] += 1

    if oper_arr[1] > 0:
        oper_arr[1] -= 1
        solution(depth + 1, oper_arr, num_arr, value - num_arr[depth])
        oper_arr[1] += 1

    if oper_arr[2] > 0:
        oper_arr[2] -= 1
        solution(depth + 1, oper_arr, num_arr, value * num_arr[depth])
        oper_arr[2] += 1

    if oper_arr[3] > 0:
        oper_arr[3] -= 1
        if value < 0:
            solution(depth + 1, oper_arr, num_arr, ((value * -1) // num_arr[depth]) * -1)
        else:
            solution(depth + 1, oper_arr, num_arr, value // num_arr[depth])
        oper_arr[3] += 1


N = int(input())
numbers = list(map(int, input().split()))

operators = list(map(int, input().split()))

solution(1, operators, numbers, numbers[0])

print(max_val)
print(min_val)
