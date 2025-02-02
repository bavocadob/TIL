import math
import sys

input = sys.stdin.readline


def solve():
    T, cmd = input().split()
    T = int(T)

    curr_opr = '+'
    left = 0
    right = 0
    curr_values = {0: 1}
    while right < len(cmd):

        while right < len(cmd) and cmd[right] != '+' and cmd[right] != '-':
            right += 1

        curr_code = cmd[left:right]
        new_values = dict()

        if 'd' in curr_code:
            dice_cnt, dice_range = map(int, curr_code.split('d'))
            plus_minus = 1 if curr_opr == '+' else -1
            for _ in range(dice_cnt):
                new_values = dict()
                for i in range(1, dice_range + 1):
                    for val, cnt in curr_values.items():
                        if val + (i * plus_minus) not in new_values:
                            new_values[val + (i * plus_minus)] = cnt
                        else:
                            new_values[val + (i * plus_minus)] += cnt
                curr_values = new_values

        else:
            num = int(curr_code)
            if curr_opr == '-':
                num *= -1
            for val, cnt in curr_values.items():
                new_values[val + num] = cnt

            curr_values = new_values
        left = right + 1
        if right != len(cmd):
            curr_opr = cmd[right]
        right += 1

    correct = max_cnt = 0
    for val, cnt in curr_values.items():
        if val >= T:
            correct += cnt
        max_cnt += cnt

    if correct == max_cnt:
        print(1)
    elif correct == 0:
        print(0)
    else:
        gcd = math.gcd(correct, max_cnt)
        print(f"{correct // gcd}/{max_cnt // gcd}")


N = int(input())

for _ in range(N):
    solve()
