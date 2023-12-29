N = int(input())

prev_digit_len = 0
digit_len = 0
digit = 0

while N > digit_len:
    prev_digit_len = digit_len
    digit_len += (9 * (10 ** (digit // 2))) * (digit + 1)

    digit += 1

digit_len -= prev_digit_len
N -= prev_digit_len

nth = ((N - 1) // digit) + 1
order = ((N - 1) % digit)

original = str((10 ** ((digit - 1) // 2)) + (nth - 1))

if digit % 2:
    original += original[:-1][::-1]
else:
    original += original[::-1]

print(original[order])
