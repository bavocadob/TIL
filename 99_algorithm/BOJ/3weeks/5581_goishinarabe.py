import sys

input = sys.stdin.readline

N = int(input())

stack = []

# 돌 번호, 사이즈

for i in range(1, N + 1):
    stone = int(input())
    if i % 2:
        if stack and stack[-1][0] == stone:
            stack[-1][1] += 1
        else:
            stack.append([stone, 1])
    else:
        if stack and stack[-1][0] == stone:
            stack[-1][1] += 1
        else:
            cnt = 0
            while stack and stack[-1][0] != stone:
                _, stone_size = stack.pop()
                cnt += stone_size

            if not stack:
                stack.append([stone, cnt + 1])
            else:
                stack[-1][1] += cnt + 1

result = 0
for s in stack:
    if s[0] == 0:
        result += s[1]

print(result)
