import sys

sys.stdin = open('input.txt')

for T in range(1, 11):
    N = int(input())
    a = input()
    stack = []
    new_stack = []

    for x in a:
        # 피연산자일 경우 푸쉬
        if x.isdecimal():
            new_stack.append(x)
        # 연산자일 경우 +-*/() 연산 우선순위에 따라 연산한다.
        else:
            if x == '(': # 여는 괄호는 그냥 연다
                stack.append(x)
            elif x == ')':
                while stack and stack[-1] != '(':  # (를 만날 때까지 연산.
                    new_stack.append(stack.pop())
                stack.pop()  # 스택에 쌓여있는 ( 없에기

            elif x == '*':
                # 스택이 비어있지 않고 스택의 마지막이 *나 /일 때
                while stack and stack[-1] == '*':
                    new_stack.append(stack.pop())
                stack.append(x)
            elif x == '+':
                while stack and stack[-1] != '(':
                    new_stack.append(stack.pop())
                stack.append(x)

    # 스택에 남아있는 것들 연산
    while stack:
        new_stack.append(stack.pop())

    # print(new_stack)

    for i in range(len(new_stack)):
        if new_stack[i].isdecimal(): # 피연산자인 경우 푸쉬
            stack.append(int(new_stack[i]))
        else:
            x, y = stack.pop(), stack.pop() # 두개를 꺼냄
            if new_stack[i] == '+':
                stack.append(x + y)
            elif new_stack[i] == '*':
                stack.append(x * y)

    print(f'#{T} {stack[0]}')


