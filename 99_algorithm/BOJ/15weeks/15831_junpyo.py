def calc(idx, opr):
    global white, black

    if stone[idx] == 'W':
        white += opr
    else:
        black += opr


N, B, W = map(int, input().split())
ans = 0

white = black = left = right = 0

stone = input().rstrip()

while right < N:
    if black <= B:
        calc(right, 1)
        right += 1
        if white >= W and black <= B:
            ans = max(ans, right - left)
    else:
        while black > B:
            calc(left, -1)
            left += 1

print(ans)
