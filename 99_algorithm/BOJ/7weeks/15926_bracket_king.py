N = int(input())

stack = [-1]

ans = 0

for i, bracket in enumerate(input()):
    if bracket == '(':
        stack.append(i)
    else:
        idx = stack.pop()
        if not stack:
            stack.append(i)
        else:
            ans = max(ans, i - stack[-1])


print(ans)
