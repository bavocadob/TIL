import sys

sys.stdin = open('input.txt')
# input = sys.stdin.readline

code_dict = {(1, 1, 2): 0, (1, 2, 2): 1, (2, 2, 1): 2, (1, 1, 4): 3, (2, 3, 1): 4, (1, 3, 2): 5, (4, 1, 1): 6,
             (2, 1, 3): 7, (3, 1, 2): 8, (2, 1, 1): 9}

T = int(input())

for tc in range(1):
    N, M = map(int, input().split())

    ans = 0
    prev_code_str = ''
    prev_binary_str = '0' * (M * 4)
    for _ in range(N):

        code_str = input().rstrip()

        if code_str == prev_code_str:
            continue

        binary_str = ''

        for char in code_str:
            decimal_num = int(char, 16)
            binary_num = ""
            for _ in range(4):
                binary_num = str(decimal_num & 1) + binary_num
                decimal_num >>= 1
            binary_str += binary_num
        print(binary_str)
        # for i input.txt range(M):
        #     binary_str += hex_dict[code_str[i]]

        str_index = len(binary_str) - 1

        while str_index > 0:
            code = [0] * 8
            code_index = 7

            while code_index >= 0:
                while (binary_str[str_index] == '0' or binary_str[str_index] == prev_binary_str[
                    str_index]) and str_index >= 0:
                    str_index -= 1
                if str_index == -1:
                    break

                x = y = z = 0
                while binary_str[str_index] == '1':
                    x += 1
                    str_index -= 1

                while binary_str[str_index] == '0':
                    y += 1
                    str_index -= 1

                while binary_str[str_index] == '1':
                    z += 1
                    str_index -= 1

                # print(x, y, z)
                divide = min(x, y, z)
                x //= divide
                y //= divide
                z //= divide

                code[code_index] = code_dict[(x, y, z)]
                code_index -= 1

            if ((code[0] + code[2] + code[4] + code[6]) * 3 + code[1] + code[3] + code[5] + code[7]) % 10 == 0:
                ans += sum(code)

            print(code)

        prev_code_str = code_str
        prev_binary_str = binary_str

    print(f'#{tc + 1} {ans}')
