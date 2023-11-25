N, K = map(int, input().split())
numbers = list(map(int, input().split()))

left = right = 0

ans = 0
d = 0

while right < N:
    if d < K:
        if numbers[right] % 2:
            d += 1
        right += 1
    elif d == K and not numbers[right] % 2:
        right += 1
    else:
        if numbers[left] % 2:
            d -= 1
        left += 1

    ans = max(ans, right - left - d)

print(ans)
