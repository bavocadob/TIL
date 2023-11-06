from collections import deque


def cpp_integer_division(dividend, divisor):
    if (dividend < 0) != (divisor < 0):
        # 두 피연산자의 부호가 다를 경우 버림 동작이 C++과 같게 하기 위해 1을 더해줌
        result = (dividend + divisor - 1) // divisor
    else:
        result = dividend // divisor
    return result


def calc_left():
    l_value = num[0]
    r_value = num[1]

    if opr[0] == '+':
        return l_value + r_value
    elif opr[0] == '-':
        return l_value - r_value
    elif opr[0] == '*':
        return l_value * r_value
    elif opr[0] == '/':
        return cpp_integer_division(l_value, r_value)


def calc_right():
    l_value = num[-2]
    r_value = num[-1]

    if opr[-1] == '+':
        return l_value + r_value
    elif opr[-1] == '-':
        return l_value - r_value
    elif opr[-1] == '*':
        return l_value * r_value
    elif opr[-1] == '/':
        return cpp_integer_division(l_value, r_value)


def execute_left(value):
    opr.popleft()
    num.popleft()
    num.popleft()
    num.appendleft(value)


def execute_right(value):
    opr.pop()
    num.pop()
    num.pop()
    num.append(value)


opr_dict = {'+': 1, '-': 1, '*': 0, '/': 0}

exp = input().rstrip()

num = deque()
opr = deque()

curr = 0
for char in exp:
    if char in opr_dict:
        num.append(curr)
        curr = 0
        opr.append(char)
    else:
        curr *= 10
        curr += int(char)

num.append(curr)

if exp[0] == '-':
    num.popleft()
    opr.popleft()
    num[0] *= -1

while opr:
    if opr_dict[opr[0]] > opr_dict[opr[-1]]:
        execute_right(calc_right())
    elif opr_dict[opr[0]] < opr_dict[opr[-1]]:
        execute_left(calc_left())
    else:
        left = calc_left()
        right = calc_right()
        if right > left:
            execute_right(right)
        else:
            execute_left(left)

print(num[0])
