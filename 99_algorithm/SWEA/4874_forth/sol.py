import sys

sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):

    formula = input().split()
    stack = []
    valid = True
    for f in formula:
        if f.isdigit():
            stack.append(f)
        else:
            if f in ['+', '*', '-', '/']:
                if len(stack) >= 2 and stack[-1].isdigit() and stack[-2].isdigit():
                    x, y = int(stack.pop()), int(stack.pop())
                    if f == '+':
                        stack.append(str(x+y))
                    elif f == '*':
                        stack.append(str(x * y))
                    elif f == '-':
                        stack.append(str(y-x))
                    elif f == '/':
                        stack.append(str(y//x))
                else:
                    valid = False
                    break

    if valid and len(stack) == 1:
        print(f'#{tc} {stack[0]}')
    else:
        print(f'#{tc} error')