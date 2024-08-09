N, T, A, B = map(int, input().split())


left = right = 0

books = [0] + list(map(int, input().split()))

for i in range(1, N + 1):
    books[i] = books[i] + books[i - 1]

curr = 0

ans = 0
while left <= right and curr <= T:
    if curr + A <= T and right < N:
        curr += A
        right += 1
        ans = max(ans, books[right] - books[left])
    else:
        left += 1
        curr -= A - B

print(ans)
