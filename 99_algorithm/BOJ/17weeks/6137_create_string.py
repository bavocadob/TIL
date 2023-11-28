import sys

input = sys.stdin.readline

N = int(input())

chars = [input().rstrip() for _ in range(N)]

left = 0
right = N - 1

result = []

while left < right:
    if chars[left] < chars[right]:  # 오른쪽이 더 늦은 알파벳이면 왼쪽 전진
        result.append(chars[left])
        left += 1
    elif chars[left] > chars[right]:  # 왼쪽이 더 늦은 알파벳이면 오른쪽 전진
        result.append(chars[right])
        right -= 1
    else:  # 두 포인터의 값이 같으면 어느쪽으로 가야 더작은지 찾아야함
        is_left = True
        inner_l = left + 1
        inner_r = right - 1
        while inner_l < inner_r:
            if chars[inner_l] == chars[inner_r]:
                inner_l += 1
                inner_r -= 1
                continue

            if chars[inner_l] > chars[inner_r]:
                is_left = False

            break

        if is_left:
            result.append(chars[left])
            left += 1
        else:
            result.append(chars[right])
            right -= 1

if len(result) < N and left == right:
    result.append(chars[left])

for i in range(N // 80 + 1):
    print(''.join(result[i * 80:(i + 1) * 80]))
