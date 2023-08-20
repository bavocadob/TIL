import sys
input = sys.stdin.readline

n = int(input())

left = right = -1_000_000_000

result = 0

for i in range(n):
    l, r = map(int, input().split())
    if l > right:
        result += r - l
        left = l
        right = r
    else:
        if r > right:
            result += r - right
            right = r

print(result)

