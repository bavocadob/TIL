import sys

sys.stdin = open('input.txt')

T = int(input())


def bin_to_dec(binary):
    binary_list = list(binary)
    result = set()
    for i in range(len(binary_list)):
        if binary_list[i] == '0':
            binary_list[i] = '1'
            result.add(int(''.join(binary_list), base=2))
            binary_list[i] = '0'
        else:
            binary_list[i] = '0'
            result.add(int(''.join(binary_list), base=2))
            binary_list[i] = '1'

    return result


def tri_to_dec(trinary):
    trinary_list = list(trinary)
    result = 0
    for i in range(len(trinary)):
        if trinary_list[i] == '0':
            trinary_list[i] = '1'
            if int(''.join(trinary_list), base=3) in binary_candidate:
                result = int(''.join(trinary_list), base=3)
                break
            trinary_list[i] = '2'
            if int(''.join(trinary_list), base=3) in binary_candidate:
                result = int(''.join(trinary_list), base=3)
                break
            trinary_list[i] = '0'
        elif trinary_list[i] == '1':
            trinary_list[i] = '0'
            if int(''.join(trinary_list), base=3) in binary_candidate:
                result = int(''.join(trinary_list), base=3)
                break
            trinary_list[i] = '2'
            if int(''.join(trinary_list), base=3) in binary_candidate:
                result = int(''.join(trinary_list), base=3)
                break
            trinary_list[i] = '1'
        else:
            trinary_list[i] = '0'
            if int(''.join(trinary_list), base=3) in binary_candidate:
                result = int(''.join(trinary_list), base=3)
                break
            trinary_list[i] = '1'
            if int(''.join(trinary_list), base=3) in binary_candidate:
                result = int(''.join(trinary_list), base=3)
                break
            trinary_list[i] = '2'

    return result


for tc in range(T):
    binary_str = input()
    trinary_str = input()

    binary_candidate = bin_to_dec(binary_str)
    print(f'#{tc + 1} {tri_to_dec(trinary_str)}')
