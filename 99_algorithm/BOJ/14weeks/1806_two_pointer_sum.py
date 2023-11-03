import sys

input = sys.stdin.readline

N, S = map(int, input().split())

numbers = list(map(int, input().split()))

left = right = 0
temp_sum = numbers[0]
ans = int(1e9)
while True:
    if temp_sum < S:
        right += 1
        if right == N:
            break

        temp_sum += numbers[right]

    if temp_sum >= S:
        ans = min(ans, right - left + 1)
        temp_sum -= numbers[left]

        left += 1

if ans != int(1e9):
    print(ans)
else:
    print(0)
