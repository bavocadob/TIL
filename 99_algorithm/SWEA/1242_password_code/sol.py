import sys

sys.stdin = open('input.txt')

hex_dict = {'0': '0000',
            '1': '0001',
            '2': '0010',
            '3': '0011',
            '4': '0100',
            '5': '0101',
            '6': '0110',
            '7': '0111',
            '8': '1000',
            '9': '1001',
            'A': '1010',
            'B': '1011',
            'C': '1100',
            'D': '1101',
            'E': '1110',
            'F': '1111'}

T = int(input())

for tc in range(1):
    N, M = map(int, input().split())

    ans = 0
    prev_code_str = ''

    for _ in range(N):
        code = [0] * 8
        code_index = 7

        code_str = input().rstrip()

        if code_str == prev_code_str:
            continue

        binary_str = ''

        for i in range(M):
            binary_str += hex_dict[code_str[i]]

