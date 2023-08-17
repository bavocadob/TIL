import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    input()
    numbers = list(map(int, input().split()))
    min_val = min(numbers) - 1
    if min_val > 15:
        for i in range(8):
            numbers[i] -= (min_val // 15) * 15

    index = 0
    minus = 1
    while True:
        if numbers[index] - minus <= 0:
            numbers[index] = 0
            break

        numbers[index] -= minus
        minus = (minus % 5) + 1
        index = (index + 1) % 8

    # print(numbers, index)
    print(f'#{tc + 1} {" ".join(map(str, numbers[index + 1:] + numbers[:index + 1]))}')
