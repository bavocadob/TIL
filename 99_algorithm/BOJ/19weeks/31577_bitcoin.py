number_lists = [
    [16, 2, 3, 14, 17, 6, 7, 8],
    [16, 2, 8, 4, 9, 10, 11, 12],
    [1, 2, 8, 4, 14, 15, 16, 20],
    [16, 2, 3, 15, 17, 18, 19, 20],
    [15, 5, 6, 7, 8, 9, 18, 19],
    [9, 4, 17, 6, 11, 12, 13, 14],
    [9, 4, 5, 6, 15, 16, 17, 18],
    [3, 4, 18, 6, 19, 20, 1, 2],
    [10, 12, 13, 14, 15, 16, 17, 19],
    [10, 11, 12, 13, 18, 19, 20, 1],
    [10, 11, 12, 13, 2, 3, 4, 5],
    [10, 11, 12, 13, 6, 7, 8, 9],
    [1, 3, 5, 7, 9, 11, 13, 15],
    [1, 3, 5, 7, 8, 10, 14, 20],
    [1, 14, 5, 7, 17, 18, 19, 20]
]

for lst in number_lists:
    print(*sorted(lst))


