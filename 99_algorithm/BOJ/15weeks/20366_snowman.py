N = int(input())

snows = list(map(int, input().split()))

snows.sort()
ans = float('inf')
for i in range(N - 3):
    for j in range(i + 3, N):
        snowman1 = snows[i] + snows[j]
        left = i + 1
        right = j - 1

        while right > left:
            if left == i:
                left += 1
                continue
            if right == j:
                right -= 1
                continue

            snowman2 = snows[left] + snows[right]
            ans = min(ans, abs(snowman1 - snowman2))
            if snowman1 > snowman2:
                left += 1
            else:
                right -= 1

print(ans)
