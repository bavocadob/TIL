N = int(input())

numbers = list(map(int, input().split()))

l = 0
r = N - 1

ans = 0
while l + 1 < r:
    ans = max(ans, (r - l - 1) * min(numbers[l], numbers[r]))
    if numbers[l] > numbers[r]:
        r -= 1
    else:
        l += 1

print(ans)
