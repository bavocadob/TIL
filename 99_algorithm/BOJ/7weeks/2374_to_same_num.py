import sys
input = sys.stdin.readline

N = int(input())

stack = []

cnt = 0
for _ in range(N):

    number = int(input())
    if not stack:
        stack.append(number)

    if stack and number == stack[-1]:
        continue

    if number < stack[-1]:  # 작은 숫자 들어오면
        stack.append(number)  # 그냥 append침
    else:  # 큰 숫자 들어오면
        cnt += number - stack.pop()
        while stack and stack[-1] <= number:
            stack.pop()
        stack.append(number)

cnt += stack[0] - stack[-1]


print(cnt)
