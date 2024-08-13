n = int(input())
a = input().strip()

prefix_sum = [0] * (n + 1)
stack = []
ans = 0

pos = 1
for i in range(1, n + 1):
    if a[i - 1] == '(':
        prefix_sum[i] = 1
    else:
        prefix_sum[i] = -1

    if i == 1:
        stack.append(a[0])
        continue

    prefix_sum[i] += prefix_sum[i - 1]

    if len(stack) == 0:
        pos = i
        stack.append(a[i - 1])
        continue

    if stack[-1] == '(' and a[i - 1] == ')':
        stack.pop()
        if len(stack) == 0:
            pos = i + 1
    else:
        stack.append(a[i - 1])

    if prefix_sum[i] - prefix_sum[pos - 1] == 0 and len(stack) > 0:
        ans += (i - pos + 1)
        pos = i + 1
        stack.clear()

if prefix_sum[n] - prefix_sum[0] != 0:
    print(-1)
else:
    print(ans)
