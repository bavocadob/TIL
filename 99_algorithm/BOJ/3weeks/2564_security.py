def solution(width, height, cp1, po1, cp2, po2):
    if cp1 == cp2:
        return abs(po1 - po2)

    # 맞닿아 있는 경우 북남 or 서동
    if (cp1 + cp2) % 4 == 3:
        if cp1 in [1, 2]:
            return height + min(po1 + po2, width * 2 - po1 - po2)
        else:
            return width + min(po1 + po2, height * 2 - po1 - po2)
    # cp1을 남북으로 고정
    if cp2 in [1, 2]:
        return solution(width, height, cp2, po2, cp1, po1)
    # cp1을 북으로 고정
    if cp1 == 2:
        return solution(width, height, 1, po1, cp2, height - po2)
    # cp2를 서쪽으로 고정
    if cp2 == 4:
        return solution(width, height, cp1, width - po1, 3, po2)

    return po1 + po2


W, H = map(int, input().split())
N = int(input())
markets = [tuple(map(int, input().split())) for _ in range(N)]
x, y = map(int, input().split())

result = 0
for xx, yy in markets:
    result += solution(W, H, x, y, xx, yy)

print(result)
