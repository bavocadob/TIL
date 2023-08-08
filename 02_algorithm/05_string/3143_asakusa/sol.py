import sys

sys.stdin = open('input.txt')


def count_without_overlap(text, substring):
    count = 0
    i = 0
    substring_len = len(substring)
    text_len = len(text)

    while i <= text_len - substring_len:
        match = True
        for j in range(substring_len):
            if text[i + j] != substring[j]:
                match = False
                break

        if match:
            count += 1
            i += substring_len
        else:
            i += 1

    return count



for T in range(int(input())):
    s, p = input().split()
    cnt_of_pattern = count_without_overlap(s, p)

    print(cnt_of_pattern)
    print(s.count(p))

    print(f'#{T + 1} {len(s) - len(p) * cnt_of_pattern + cnt_of_pattern}')
