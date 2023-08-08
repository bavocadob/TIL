# import sys
#
# sys.stdin = open('input.txt')

def count_without_overlap(text, pattern):
    count = 0
    i = 0
    pattern_len = len(pattern)
    text_len = len(text)

    while i <= text_len - pattern_len:
        match = True
        for j in range(pattern_len):
            if text[i + j] != pattern[j]:
                match = False
                break

        if match:
            count += 1
            i += pattern_len
        else:
            i += 1

    return count


if __name__ == '__main__':
    for _ in range(1, 11):
        T = input()
        p = input()
        s = input()
        cnt_of_pattern = count_without_overlap(s, p)

        print(f'#{T} {cnt_of_pattern}')
