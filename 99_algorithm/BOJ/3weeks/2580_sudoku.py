def solution(depth):
    if depth == len_zero_index:
        for line in sudoku_arr:
            print(*line)
        exit(0)
        return

    x, y = zero_index_arr[depth]

    for i in range(1, 10):
        r_flag = True
        c_flag = True
        s_flag = True
        nx = x // 3 * 3
        ny = y // 3 * 3
        for j in range(9):
            if sudoku_arr[x][j] == i:
                r_flag = False
                break
            if sudoku_arr[j][y] == i:
                c_flag = False
                break
            if sudoku_arr[nx + (j // 3)][ny + (j % 3)] == i:
                s_flag = False
                break

        if r_flag and c_flag and s_flag:
            sudoku_arr[zero_index_arr[depth][0]][zero_index_arr[depth][1]] = i
            solution(depth + 1)
            sudoku_arr[zero_index_arr[depth][0]][zero_index_arr[depth][1]] = 0
    else:
        return


sudoku_arr = []

zero_index_arr = []

end = False

for i in range(9):
    sudoku_str = list(map(int, input().split()))
    zero_len = sudoku_str.count(0)
    if zero_len == 1:
        sudoku_str[sudoku_str.index(0)] = 45 - sum(sudoku_str)
    sudoku_arr.append(sudoku_str)

for i in range(9):
    h_count = 0
    v_count = 0
    s_count = 0
    h_index = None
    v_index = None
    s_index = None
    for j in range(9):
        if sudoku_arr[i][j] == 0:
            h_count += 1
            h_index = (i, j)
        if sudoku_arr[j][i] == 0:
            v_count += 1
            v_index = (j, i)
        if sudoku_arr[i // 3][j % 3] == 0:
            s_count += 1
            s_index = (i // 3, j % 3)

    if h_count == 1:
        temp_sum = 0
        for k in range(9):
            temp_sum += sudoku_arr[i][k]
        sudoku_arr[h_index[0]][h_index[1]] = 45 - temp_sum

    if v_count == 1:
        temp_sum = 0
        for k in range(9):
            temp_sum += sudoku_arr[k][i]
        sudoku_arr[v_index[0]][v_index[1]] = 45 - temp_sum

    if s_count == 1:
        temp_sum = 0
        for k in range(9):
            temp_sum += sudoku_arr[i // 3][k % 3]
        sudoku_arr[s_index[0]][s_index[1]] = 45 - temp_sum

for i in range(9):
    for j in range(9):
        if sudoku_arr[i][j] == 0:
            zero_index_arr.append((i, j))

len_zero_index = len(zero_index_arr)

solution(0)

# for line input.txt sudoku_str:
#     print(line)
#
# print(zero_index_arr)
