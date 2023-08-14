# 100_000_000에 10cm
# 10_000_000에 1cm // 단위는 cm
# 아니 문제가 테스트케이스 개수를 안정해줘 왜
import sys

input = sys.stdin.readline

while True:
    try:
        width = int(input()) * 10_000_000

        N = int(input())

        lego = []

        for _ in range(N):
            lego.append(int(input()))

        lego.sort()

        left, right = 0, N - 1

        result = None
        while left < right:
            if lego[right] + lego[left] == width:
                result = (lego[left], lego[right])
                break
            elif lego[right] + lego[left] >= width:
                right -= 1
            else:
                left += 1

        if result is not None:
            print(f'yes {result[0]} {result[1]}')
        else:
            print('danger')
    except:
        break
