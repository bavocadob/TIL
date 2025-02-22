import sys

input = sys.stdin.readline


def convert(year: int, month: int):
    return (year - 2000) * 12 + (month - 1)


def convert_reverse(date_idx: int):
    year = (date_idx // 12) + 2000
    month = (date_idx % 12) + 1
    return f'{year}-{month:02d}'


N = int(input())

prefix_sum = [0] * (10000 * 12)
for _ in range(N):
    start, end = input().split()

    s_year, s_month = map(int, start.split('-'))
    e_year, e_month = map(int, end.split('-'))

    s_pos = convert(s_year, s_month)
    e_pos = convert(e_year, e_month)

    prefix_sum[s_pos] += 1
    prefix_sum[e_pos + 1] -= 1

ans = 0
ans_pos = 0

for i in range(10000 * 12):
    prefix_sum[i] += prefix_sum[i - 1]

    if prefix_sum[i] > ans:
        ans = prefix_sum[i]
        ans_pos = i

print(convert_reverse(ans_pos))
