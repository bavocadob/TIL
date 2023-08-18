def solution(x1, y1, x2, y2, x3, y3, x4, y4):
    # 공통부분이 없는 경우
    if x2 < x3 or x1 > x4 or y1 > y4 or y2 < y3:
        return 'd'
    # 공통부분이 하나만 있는 경우 (점이 맞닿는 경우)
    elif (x2 == x3 or x4 == x1) and (y2 == y3 or y4 == y1):
        return 'c'
    # 공통부분이 선분인 경우
    elif (y1 == y4 or y3 == y2) or (x2 == x3 or x4 == x1):
        return 'b'
    # 공통부분이 직사각형인 경우
    else:
        return 'a'


for _ in range(4):
    a1, b1, a2, b2, a3, b3, a4, b4 = map(int, input().split())
    print(solution(a1, b1, a2, b2, a3, b3, a4, b4))
