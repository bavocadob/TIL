import sys

input = sys.stdin.readline

N = int(input())

stack = [0]

ans = 0

for _ in range(N):
    x, y = map(int, input().split())

    while stack[-1] > y:
        stack.pop()
        ans += 1

    if y > stack[-1]:
        stack.append(y)

ans += len(stack) - 1

print(ans)
